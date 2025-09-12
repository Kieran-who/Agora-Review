from logger import get_logger
from typing import Any, List
from utils.tokenizer import TokenRequest, handle_token_request
from openai import AzureOpenAI
from embeddings.models import EmbeddingRequest, EmbeddingResponse, EmbeddingUsage
from telemetry import telemetry_custom
# ---------------- Configuration & Interfaces ---------------- #
from embeddings.models import AzureEmbeddingProviderConfig

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

class AzureEmbeddingProvider:    
    def __init__(
        self,
        config: AzureEmbeddingProviderConfig,
        *,
        request_timeout: float = 30.0,
        max_retries: int = 10,
        backoff_base: float = 0.8
    ) -> None:        
        self.api_key = config.api_key
        if not config.api_key:
            raise AuthError("Missing Azure OpenAI API key.")
        if not config.resource_name:
            raise ValueError("Missing Azure OpenAI resource name.")
        if not config.deployment_name:
            raise ValueError("Missing Azure OpenAI deployment name.")
        self.client = AzureOpenAI(
            api_key=config.api_key,
            azure_endpoint=f"https://{config.resource_name}.openai.azure.com/",
            max_retries=max_retries,
            timeout=request_timeout,
            api_version=config.api_version
        ) 
        self.deployment_name = config.deployment_name
        self.vector_length = config.vector_length
        self.max_retries = max_retries
        self.backoff_base = backoff_base
        self.log = get_logger(__name__)

    def generate(self, request: EmbeddingRequest) -> EmbeddingResponse:
        token_request = TokenRequest(
            text=request.text,
            number=request.max_text_tokens
        )
        truncated = handle_token_request(token_request)

        response = self.client.embeddings.create(
            input=truncated.text,
            model=self.deployment_name,
            dimensions=self.vector_length
        )
        
        embedding: List[float] = response.data[0].embedding
        
        usage = EmbeddingUsage(
            prompt_tokens=response.usage.prompt_tokens,
            total_tokens=response.usage.total_tokens,
        )

        self._send_telemetry(usage)

        return EmbeddingResponse(
            embedding=embedding,
            usage=usage,
            model_used=self.deployment_name,
            provider="azure",
        )

    def _send_telemetry(self, usage: EmbeddingUsage):
        model_identifier = f"azure_{self.deployment_name}"
        attrs = {"model": model_identifier, "provider": "azure"}
        telemetry_custom.send_metric("new_vector", 1, {**attrs})
        telemetry_custom.send_metric("ai_tokens_prompt", usage.prompt_tokens, attrs)
