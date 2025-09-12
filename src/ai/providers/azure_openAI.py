from logger import get_logger
from typing import Any, List
from utils.tokenizer import ChatTokenRequest, handle_chat_token_request
from openai import AzureOpenAI
from openai.types.responses.response_input_param import ResponseInputParam, FunctionCallOutput
from openai.types.responses.easy_input_message_param import EasyInputMessageParam
from openai.types.responses.response_function_tool_call_param import ResponseFunctionToolCallParam
from openai.types.responses.response import Response
from telemetry import telemetry_custom
from config import CONFIG
# ---------------- Configuration & Interfaces ---------------- #
from ai.models import AzureLLMProviderConfig, LMMRequest, Usage, ChatMessage

# ---------------- Errors ---------------- #

class AIError(Exception):
    def __init__(self, message: str, provider: str = "azure", meta: Any = None):
        super().__init__(message)
        self.provider = provider
        self.meta = meta

class ApiError(AIError):
    def __init__(self, message: str, status_code: int, provider: str = "azure", meta: Any = None):
        super().__init__(message, provider, meta)
        self.status_code = status_code

class AuthError(AIError):
    pass

class RateLimitError(AIError):
    pass

# ---------------- Provider ---------------- #

class AzureLLMProvider:    
    def __init__(
        self,
        config: AzureLLMProviderConfig,
        *,
        request_timeout: float = 120.0,
        max_retries: int = 10
    ) -> None:        
        self.api_key = config.api_key
        if not config.api_key:
            raise AuthError("Missing Azure OpenAI API key.")
        if not config.resource_name:
            raise ValueError("Missing Azure OpenAI resource name.")
                
        self.client = AzureOpenAI(
            api_key=config.api_key,
            azure_endpoint=f"https://{config.resource_name}.openai.azure.com/",
            max_retries=max_retries,
            timeout=request_timeout,
            api_version=config.api_version,
        )
        self.config = config
        self.log = get_logger(__name__)

    def _format_messages(self, messages: List[ChatMessage]) -> ResponseInputParam:
        formatted_messages: ResponseInputParam = []
        for message in messages:
            if message.role == 'tool' and message.tool_call_id and message.tool_output:
                formatted_messages.append(FunctionCallOutput(
                    call_id=message.tool_call_id,
                    output=message.tool_output,
                    type="function_call_output",
                ))
            elif message.role == 'assistant':
                if message.tool_calls:                    
                    for tc in message.tool_calls:
                        formatted_messages.append(ResponseFunctionToolCallParam(
                            call_id=tc.id,
                            arguments=tc.function.arguments,
                            name=tc.function.name,
                            type="function_call",
                        ))
                elif message.content:
                    formatted_messages.append(EasyInputMessageParam(
                        role=message.role,
                        content=message.content
                    ))
            elif (message.role == 'user' or message.role == 'system') and message.content:
                formatted_messages.append(EasyInputMessageParam(
                    role=message.role,
                    content=message.content
                ))
        return formatted_messages

    def generate(self, request: LMMRequest) -> Response:
        truncated = handle_chat_token_request(
            ChatTokenRequest(messages=request.messages, number=CONFIG.max_chat_tokens)
        )
        
        result = self.client.responses.create(
            model=self.config.large_model_deployment if request.model_size == 'large' else self.config.small_model_deployment,
            tools=request.tool_calls,
            tool_choice='auto' if not request.require_tool_use else 'required',
            input=self._format_messages(truncated.messages),
            parallel_tool_calls=False,
            store=False
        )

        if result.usage:
            usage = Usage(
                prompt_tokens=result.usage.input_tokens,
                completion_tokens=result.usage.output_tokens,
                total_tokens=result.usage.total_tokens,
                cached_tokens=result.usage.input_tokens_details.cached_tokens,
                model_size=request.model_size
            )

            self._send_telemetry(usage)

        return result

    def _send_telemetry(self, usage: Usage):
        model_identifier = f"azure_{usage.model_size}"
        attrs = {"model": model_identifier, "provider": "azure"}
        telemetry_custom.send_metric("model_response", 1, {**attrs})
        telemetry_custom.send_metric("ai_tokens_prompt", usage.prompt_tokens, attrs)
        telemetry_custom.send_metric("ai_tokens_completion", usage.completion_tokens, attrs)
        telemetry_custom.send_metric("ai_tokens_total", usage.total_tokens, attrs)
        telemetry_custom.send_metric("ai_tokens_cached", usage.cached_tokens, attrs)