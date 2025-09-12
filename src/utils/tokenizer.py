
from logger import get_logger
from typing import List, Tuple, Optional
import tiktoken
from dataclasses import dataclass
# Import unified models from the models file
from ai.models import ChatMessage

logger = get_logger(__name__)

@dataclass(frozen=True)
class ChatTokenResponse:
    """Response for a chat tokenization request, returning the potentially pruned messages."""
    messages: List[ChatMessage]
    token_count: int

@dataclass(frozen=True)
class ChatTokenRequest:
    """Request to calculate and truncate tokens for a list of chat messages."""
    messages: List[ChatMessage]
    number: int
    model: Optional[str] = 'gpt-4o'

@dataclass(frozen=True)
class TokenRequest:
    text: str
    number: int
    model: Optional[str] = 'text-embedding-3-small'

@dataclass(frozen=True)
class TokenResponse:
    text: str
    number: int    

# --- Constants ---

# Default models and encodings
DEFAULT_CHAT_MODEL = "gpt-4o" # gpt-5 not supported
DEFAULT_ENCODING = "cl100k_base"
FALLBACK_ENCODING = "o200k_base"

# Token counting constants based on OpenAI's cookbook
TOKENS_PER_MESSAGE = 3
TOKENS_PER_NAME = 1
TOKENS_PER_TOOL_CALL_BASE = 4

# --- Private Helper Functions ---

def _get_encoding(model_name: str) -> tiktoken.Encoding:
    """
    Retrieves the tiktoken encoding for a given model name.
    Falls back to a default encoding if the model-specific one is not found.
    """
    try:
        return tiktoken.encoding_for_model(model_name)
    except KeyError:
        logger.warning(
            f"Encoding for model '{model_name}' not found. "
            f"Falling back to '{DEFAULT_ENCODING}' encoding."
        )
        return tiktoken.get_encoding(DEFAULT_ENCODING)
    
def _drop_orphan_tool_outputs(messages: List[ChatMessage]) -> List[ChatMessage]:
    # Build set of function_call IDs introduced by assistant messages
    call_ids: set[str] = set()
    for m in messages:
        if m.role == "assistant" and m.tool_calls:
            for tc in m.tool_calls:
                if tc and tc.id:
                    call_ids.add(tc.id)

    # Keep only tool outputs whose call_id is present in call_ids
    pruned: List[ChatMessage] = []
    for m in messages:
        if m.role == "tool" and m.tool_call_id:
            if m.tool_call_id in call_ids:
                pruned.append(m)
            # else drop orphan tool output
        else:
            pruned.append(m)
    return pruned

def _calculate_chat_tokens(
    messages: List[ChatMessage], encoding: tiktoken.Encoding
) -> int:
    """
    Calculates the total number of tokens for a list of chat messages.

    Args:
        messages: A list of ChatMessage objects.
        encoding: The tiktoken encoding to use.

    Returns:
        The total token count.
    """
    num_tokens = 3  # Every reply is primed with <|start|>assistant<|message|>
    for message in messages:
        num_tokens += TOKENS_PER_MESSAGE
        if message.role:
            num_tokens += len(encoding.encode(message.role))
        if message.name:
            num_tokens += TOKENS_PER_NAME
            num_tokens += len(encoding.encode(message.name))
        if message.tool_call_id:
            num_tokens += len(encoding.encode(message.tool_call_id))
        if message.content:            
            num_tokens += len(encoding.encode(message.content))            
        if message.tool_calls:
            for tool_call in message.tool_calls:
                num_tokens += TOKENS_PER_TOOL_CALL_BASE
                num_tokens += len(encoding.encode(tool_call.function.name))
                num_tokens += len(encoding.encode(tool_call.function.arguments))

    return num_tokens

def _is_protected_message(message: ChatMessage) -> bool:
    """Checks if a message is a system message that should not be pruned."""
    return message.role == "system"

def _prune_messages_to_fit(
    messages: List[ChatMessage], max_tokens: int, encoding: tiktoken.Encoding
) -> Tuple[List[ChatMessage], int]:
    """
    Removes messages from a conversation until the total token count is within the limit.

    Pruning strategy:
    1. Remove non-protected system messages.
    2. Remove the oldest user/assistant/tool messages.
    3. If still over limit, truncate the content of the last user message.

    Args:
        messages: The list of ChatMessage objects to prune.
        max_tokens: The maximum allowed token count.
        encoding: The tiktoken encoding to use.

    Returns:
        A tuple containing the pruned list of messages and their new total token count.
    """
    mutable_messages = list(messages)
    total_tokens = _calculate_chat_tokens(mutable_messages, encoding)

    # Strategy 1 & 2: Remove whole messages
    while total_tokens > max_tokens:
        # First, try to remove non-protected system messages
        non_protected_system_indices = [
            i for i, m in enumerate(mutable_messages) if not _is_protected_message(m) and m.role == "system"
        ]
        if non_protected_system_indices:
            del mutable_messages[non_protected_system_indices[0]]
            total_tokens = _calculate_chat_tokens(mutable_messages, encoding)
            continue
        
        # Next, remove the oldest user, assistant, or tool messages
        prunable_roles = {"user", "assistant", "tool"}
        # If there's only one user message, protect it from deletion
        if len([m for m in mutable_messages if m.role == 'user']) <= 1:
            prunable_roles.remove("user")
        
        prunable_indices = [i for i, m in enumerate(mutable_messages) if m.role in prunable_roles]

        if not prunable_indices:
            # No more messages to remove, break to move to truncation
            break
        
        del mutable_messages[prunable_indices[0]]
        total_tokens = _calculate_chat_tokens(mutable_messages, encoding)

    # Strategy 3: Truncate the last user message if still over limit
    if total_tokens > max_tokens:
        for i in range(len(mutable_messages) - 1, -1, -1):
            msg = mutable_messages[i]
            if msg.role == "user" and isinstance(msg.content, str) and msg.content:
                tokens_to_remove = total_tokens - max_tokens
                encoded_content = encoding.encode(msg.content)
                if len(encoded_content) > tokens_to_remove:
                    truncated_tokens = encoded_content[:len(encoded_content) - tokens_to_remove]
                    msg.content = encoding.decode(truncated_tokens)
                    total_tokens = _calculate_chat_tokens(mutable_messages, encoding)
                    break # Exit after truncating one message
        else: # This else belongs to the for loop, executes if loop finishes without break
            logger.error("Could not reduce token count below max_tokens by truncation.")
            raise ValueError("Unable to fit messages within the token limit.")

    mutable_messages = _drop_orphan_tool_outputs(mutable_messages)
    total_tokens = _calculate_chat_tokens(mutable_messages, encoding)
    return mutable_messages, total_tokens


# --- Public Service Functions ---

def handle_chat_token_request(
    chat_token_request: ChatTokenRequest,
) -> ChatTokenResponse:
    """
    Processes a chat tokenization request, pruning messages if necessary to fit
    within the specified token limit.

    Args:
        chat_token_request: The request with messages, token limit, and model.

    Returns:
        A ChatTokenResponse with the pruned messages and their final token count.
    """    
    model = chat_token_request.model or DEFAULT_CHAT_MODEL
    encoding = _get_encoding(model)

    pruned_messages, final_token_count = _prune_messages_to_fit(
        messages=chat_token_request.messages,
        max_tokens=chat_token_request.number,
        encoding=encoding,
    )

    return ChatTokenResponse(
        messages=pruned_messages, token_count=final_token_count
    )

def handle_token_request(
    token_request: TokenRequest,
) -> TokenResponse:
    """
    Processes a tokenization request for plain text, truncating if necessary to fit
    within the specified token limit.

    Args:
        token_request: The request with text, token limit, and model.   
    Returns:
        A TokenRequest with the potentially truncated text and its final token count.   
    """    
    model = token_request.model or 'text-embedding-3-small'
    encoding = _get_encoding(model)

    encoded_text = encoding.encode(token_request.text)
    if len(encoded_text) > token_request.number:
        truncated_tokens = encoded_text[:token_request.number]
        truncated_text = encoding.decode(truncated_tokens)
        return TokenResponse(
            text=truncated_text,
            number=len(truncated_tokens)
        )
    else:
        return TokenResponse(
            text=token_request.text,
            number=len(encoded_text)
        )