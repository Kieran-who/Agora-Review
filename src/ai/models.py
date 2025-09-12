from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Optional, Literal, List
import json

from pydantic import BaseModel, field_validator
from openai.types.responses.function_tool_param import FunctionToolParam

__all__ = [
    "AzureLLMProviderConfig",
    "GoogleLLMProviderConfig",
    "LocalLLMProviderConfig",
    "OpenAILLMProviderConfig",
    "LMMConfigError",
    "ToolFunction",
    "ToolCall",
    "ChatMessage",
    "LMMRequest",
    "Usage",
    "Turn",
    "ChatState",
]


# ---------------- Provider Configs ----------------

@dataclass(frozen=True)
class AzureLLMProviderConfig:
    large_model_deployment: str
    small_model_deployment: str
    resource_name: str
    api_version: str
    api_key: Optional[str] = None


@dataclass(frozen=True)
class GoogleLLMProviderConfig:
    large_model: str
    small_model: str
    api_key: Optional[str] = None


@dataclass(frozen=True)
class LocalLLMProviderConfig:
    large_model: str
    small_model: str


@dataclass(frozen=True)
class OpenAILLMProviderConfig:
    large_model: str
    small_model: str
    api_key: Optional[str] = None


class LMMConfigError(Exception):
    """Raised when LLM provider configuration is invalid."""
    pass


# ---------------- Pydantic Models for Tool/Message I/O ----------------

class ToolFunction(BaseModel):
    """
    A function (tool) that the model can call.
    The `arguments` field is a JSON-serialised string; validated at construction time.
    """
    name: str
    arguments: str

    @field_validator("arguments")
    @classmethod
    def _must_be_valid_json(cls, v: str) -> str:
        try:
            json.loads(v)
        except (TypeError, ValueError) as e:
            raise ValueError("`arguments` must be a JSON-serialised string") from e
        return v

    def parsed_args(self) -> Any:
        """Convenience accessor that parses `arguments` JSON to a Python object."""
        return json.loads(self.arguments)


class ToolCall(BaseModel):
    """
    Represents a tool call requested by the model, including its unique id and function payload.
    """
    id: str
    type: Literal["function"]
    function: ToolFunction

class ImgContent(BaseModel):
    type: Literal["image_url"]
    image_url: dict[Literal['url'], str]

class ChatMessage(BaseModel):
    """
    Represents a single message in a chat conversation.

    - role: "system" | "user" | "assistant" | "tool"
    - content: plain text (only for system/user/assistant content messages)
    - tool_calls: populated when the assistant requests function calls
    - tool_call_id/tool_output: populated for tool outputs (function_call_output)
    """
    role: Literal["system", "user", "assistant", "tool"]
    content: Optional[str | ImgContent] = None
    name: Optional[str] = None
    tool_call_id: Optional[str] = None
    tool_calls: Optional[List[ToolCall]] = None
    tool_output: Optional[str] = None


class LMMRequest(BaseModel):
    """
    Request envelope for the LLM provider.
    """
    model_size: Literal["small", "large"]
    messages: List[ChatMessage]
    tool_calls: list[FunctionToolParam]
    use_grounding: bool = False
    max_tokens: Optional[int] = 20000
    temperature: Optional[float] = 1.0
    require_tool_use: bool = False  # if True, the model must use a tool call    


class Usage(BaseModel):
    prompt_tokens: int
    completion_tokens: int
    cached_tokens: int
    total_tokens: int
    model_size: Literal["small", "large"]

# ---------------- Dataclasses for Conversation State ----------------
# Typed default factories to satisfy static analyzers and avoid "list[Unknown]" warnings.

def _empty_str_list() -> list[str]:
    return []

def _empty_message_list() -> list[ChatMessage]:
    return []

def _empty_turn_list() -> list["Turn"]:
    return []


@dataclass
class Turn:
    """
    One logical QA turn in the conversation.
    - numeric_value: the computed numeric result if any (e.g., 206588.0 or 0.141)
    - citations: list of CIDs like 'T[r1][c6]' used to support the answer
    """
    question: str
    answer: str
    numeric_value: Optional[float] = None
    citations: list[str] = field(default_factory=_empty_str_list)


@dataclass
class ChatState:
    """
    Mutable state for a chat session.
    - messages: the message history used by the provider (system/user/assistant/tool)
    - turns: logical QA turns with numeric/citations metadata
    """
    record_id: str
    messages: list[ChatMessage] = field(default_factory=_empty_message_list)
    turns: list[Turn] = field(default_factory=_empty_turn_list)

    def append_turn(self, *, question: str, answer: str, numeric_value: Optional[float], citations: list[str]) -> None:
        self.turns.append(Turn(question=question, answer=answer, numeric_value=numeric_value, citations=citations))