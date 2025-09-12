from logger import get_logger
from typing import Any, List
from utils.tokenizer import ChatTokenRequest, handle_chat_token_request
from google import genai
import json
from google.genai.types import Content, FunctionResponse, Part, FunctionCall, GenerateContentResponse, GenerateContentConfig, Tool, FunctionDeclaration, FunctionCallingConfig, FunctionCallingConfigMode, ToolConfig, GoogleSearch
from telemetry import telemetry_custom
from config import CONFIG
# ---------------- Configuration & Interfaces ---------------- #
from ai.models import GoogleLLMProviderConfig, LMMRequest, Usage, ChatMessage, FunctionToolParam

# ---------------- Errors ---------------- #

class AIError(Exception):
    def __init__(self, message: str, provider: str = "google", meta: Any = None):
        super().__init__(message)
        self.provider = provider
        self.meta = meta

class ApiError(AIError):
    def __init__(self, message: str, status_code: int, provider: str = "google", meta: Any = None):
        super().__init__(message, provider, meta)
        self.status_code = status_code

class AuthError(AIError):
    pass

class RateLimitError(AIError):
    pass

# ---------------- Provider ---------------- #

class GoogleLLMProvider:    
    def __init__(
        self,
        config: GoogleLLMProviderConfig,
        *,
        request_timeout: float = 30.0,
        max_retries: int = 10
    ) -> None:        
        self.api_key = config.api_key
        if not config.api_key:
            raise AuthError("Missing Google API key.")        
                
        self.client = genai.Client(api_key=config.api_key)
        self.config = config
        self.log = get_logger(__name__)

    def _format_messages(self, messages: List[ChatMessage]) -> list[Content]:
        formatted_messages: list[Content] = []
        for message in messages:
            if message.role == 'tool' and message.tool_call_id and message.tool_output:
                formatted_messages.append(Content(
                    parts =[Part(
                        function_response=FunctionResponse(
                            name=message.name,
                            response=json.loads(message.tool_output)
                        )
                    )]
                ))
            elif message.role == 'assistant':
                if message.tool_calls:
                    for tc in message.tool_calls:
                        formatted_messages.append(Content(
                            parts =[Part(
                                function_call=FunctionCall(
                                    name=tc.function.name,
                                    args=json.loads(tc.function.arguments)
                                )
                            )],
                            role=message.role
                        ))
                elif message.content:
                    formatted_messages.append(Content(
                            parts =[Part(
                                text=message.content
                            )],
                            role=message.role
                        ))                    
            elif (message.role == 'user' or message.role == 'system') and message.content:                
                formatted_messages.append(Content(
                            parts =[Part(
                                text=message.content,
                            )],
                            role=message.role
                        )) 
        return formatted_messages

    def _format_tools(self, tools: list[FunctionToolParam], use_grounding: bool = False) -> list[Tool]:
            g_tools: list[Tool] = []

            for tool in tools:
                g_tools.append(
                    Tool(
                        function_declarations=[
                            FunctionDeclaration(
                                name=tool["name"],
                                description=tool.get("description"),
                                parameters_json_schema=tool.get("parameters")
                            )
                        ]
                    )
                )
            if use_grounding:
                g_tools.append(
                    Tool(
                        google_search=GoogleSearch()
                    )
                )

            return g_tools
    
    def _create_config(self, request: LMMRequest) -> GenerateContentConfig:
        tools = None
        if request.tool_calls or request.use_grounding:
            tools = self._format_tools(request.tool_calls, request.use_grounding)
        return GenerateContentConfig(
            max_output_tokens=request.max_tokens, 
            temperature=request.temperature, 
            tools=tools,
            tool_config=ToolConfig(
                function_calling_config=FunctionCallingConfig(mode=FunctionCallingConfigMode.ANY)
            ) if request.tool_calls else None
        )

    def generate(self, request: LMMRequest) -> GenerateContentResponse:
        truncated = handle_chat_token_request(
            ChatTokenRequest(messages=request.messages, number=CONFIG.max_chat_tokens)
        )
        
        result = self.client.models.generate_content( # type: ignore
            model=self.config.large_model if request.model_size == "large" else self.config.small_model,
            contents=self._format_messages(truncated.messages),
            config=self._create_config(request)
        )

        if result.usage_metadata:
            usage = Usage(
                prompt_tokens=result.usage_metadata.prompt_token_count if result.usage_metadata.prompt_token_count else 0,
                completion_tokens=result.usage_metadata.candidates_token_count if result.usage_metadata.candidates_token_count else 0,
                total_tokens=result.usage_metadata.total_token_count if result.usage_metadata.total_token_count else 0,
                cached_tokens=result.usage_metadata.cached_content_token_count if result.usage_metadata.cached_content_token_count else 0,
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