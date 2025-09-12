from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Literal
import os

from ai.models import AzureLLMProviderConfig, OpenAILLMProviderConfig, GoogleLLMProviderConfig, LocalLLMProviderConfig

from embeddings.models import AzureEmbeddingProviderConfig

from dotenv import load_dotenv

__all__ = [
    "Config",
    "load_config",
    "WeaviateConfig",
]

# ---- Data models -----------------------------------------------------------------
@dataclass(frozen=True)
class WeaviateConfig:
    http_host: str
    http_port: int
    http_secure: bool
    grpc_host: str
    grpc_port: int
    grpc_secure: bool
    api_key: str
    weaviate_version: str
    
    def make_auth(self):
        # Import lazily to avoid import-time side-effects and hard dependency here
        from weaviate.auth import AuthApiKey
        return AuthApiKey(self.api_key)

@dataclass(frozen=True)
class LLMProviderConfig:
    azure: AzureLLMProviderConfig
    google: GoogleLLMProviderConfig
    openai: OpenAILLMProviderConfig | None = None    
    local: LocalLLMProviderConfig | None = None    

@dataclass(frozen=True)
class LLMConfig:    
    configs: LLMProviderConfig

@dataclass(frozen=True)
class Config:
    service_name: str
    prometheus_port: int
    logging_level: str
    llm_config: LLMConfig
    max_chat_tokens: int
    max_workers: int
    weaviate: WeaviateConfig
    embeddings_config: AzureEmbeddingProviderConfig
    mistral_api_key: str

# ---- Helpers ---------------------------------------------------------------------

def _get_env(mapping: Mapping[str, str] | None) -> Mapping[str, str]:
    # Allow injecting a custom env (e.g. for testing)
    return mapping if mapping is not None else os.environ

def _get_int(raw: str | None, default: int) -> int:
    if raw is None:
        return default
    try:
        return int(raw)
    except ValueError:
        return default

# ---- LLM provider builders -------------------------------------------------------
def _build_azure_config(e: Mapping[str, str]) -> AzureLLMProviderConfig:
    resource_name = e.get("AZURE_OPENAI_RESOURCE_NAME") or e.get("AZURE_OPENAI_RESOURCE")
    if not resource_name:
        raise ValueError("AZURE_OPENAI_RESOURCE_NAME is required for MODEL_PROVIDER=azure")

    small_model_deployment = e.get("AZURE_OPENAI_SMALL_DEPLOYMENT_NAME") or e.get("AZURE_OPENAI_DEPLOYMENT_NAME")
    if not small_model_deployment:
        raise ValueError("AZURE_OPENAI_SMALL_DEPLOYMENT_NAME is required for MODEL_PROVIDER=azure")
    
    large_model_deployment = e.get("AZURE_OPENAI_LARGE_DEPLOYMENT_NAME") or e.get("AZURE_OPENAI_DEPLOYMENT_NAME")
    if not large_model_deployment:
        raise ValueError("AZURE_OPENAI_LARGE_DEPLOYMENT_NAME is required for MODEL_PROVIDER=azure")

    api_version = e.get("AZURE_OPENAI_API_VERSION", "2025-03-01-preview")    

    # Accept several common key names; prefer the Azure-specific one
    api_key = (
        e.get("AZURE_OPENAI_API_KEY")
        or e.get("AZURE_API_KEY")
    )    

    return AzureLLMProviderConfig(
        resource_name=resource_name,
        small_model_deployment=small_model_deployment,
        large_model_deployment=large_model_deployment,
        api_version=api_version,        
        api_key=api_key
    )

def _build_google_config(e: Mapping[str, str]) -> GoogleLLMProviderConfig:
    # Support both names; default to a widely-used legacy model unless explicitly set
    large_model = e.get("GOOGLE_LARGE_MODEL_NAME") or "gemini-2.5-pro"
    small_model = e.get("GOOGLE_SMALL_MODEL_NAME") or "gemini-2.5-flash"
    api_key = e.get("GOOGLE_API_KEY") or e.get("GOOGLE_GENAI_API_KEY")    

    return GoogleLLMProviderConfig(
        large_model=large_model,
        small_model=small_model,
        api_key=api_key
    )

def _build_llm_config(e: Mapping[str, str]) -> LLMConfig:
   
    azure_cfg = _build_azure_config(e)    
    google_cfg = _build_google_config(e)
         
    return LLMConfig(configs=LLMProviderConfig(azure=azure_cfg, google=google_cfg))

# ---- Embeddings provider builders ---------------------------------------------------
def _infer_default_vector_length(provider: Literal["openai", "azure", "google", "local"], model_or_deployment: str) -> int:
    m = (model_or_deployment or "").lower()
    # Heuristics with safe defaults; can be overridden via env vars
    if provider in {"openai", "azure"}:
        if "3-large" in m or "embedding-3-large" in m:
            return 3072
        # ada-002 and 3-small are 1536
        return 1536   
    return 1536

def _build_azure_embedding_config(e: Mapping[str, str]) -> AzureEmbeddingProviderConfig:
    resource_name = e.get("AZURE_OPENAI_RESOURCE_NAME") or e.get("AZURE_OPENAI_RESOURCE")
    if not resource_name:
        raise ValueError("AZURE_OPENAI_RESOURCE_NAME is required for EMBEDDINGS_PROVIDER=azure")

    deployment_name = e.get("AZURE_OPENAI_EMBED_DEPLOYMENT_NAME") or e.get("AZURE_OPENAI_DEPLOYMENT_NAME")
    if not deployment_name:
        raise ValueError("AZURE_OPENAI_EMBED_DEPLOYMENT_NAME is required for EMBEDDINGS_PROVIDER=azure")

    api_version = e.get("AZURE_OPENAI_API_VERSION", "2023-05-15")
    max_text_tokens = _get_int(e.get("AZURE_OPENAI_MAX_TEXT_TOKENS", "8191"), 8191)

    # Accept several common key names; prefer the Azure-specific one
    api_key = (
        e.get("AZURE_OPENAI_API_KEY")
        or e.get("AZURE_API_KEY")
        or e.get("OPENAI_API_KEY")
    )

    default_vec_len = _infer_default_vector_length("azure", deployment_name)
    vector_length = _get_int(e.get("AZURE_OPENAI_EMBED_VECTOR_LENGTH"), default_vec_len)

    return AzureEmbeddingProviderConfig(
        resource_name=resource_name,
        deployment_name=deployment_name,
        api_version=api_version,
        max_text_tokens=max_text_tokens,
        api_key=api_key,
        vector_length=vector_length,
    )


# ---- Public loader ---------------------------------------------------------------

def load_config(env: Mapping[str, str] | None = None) -> Config:
    """
    Build a strongly-typed Config from environment variables.

    load_dotenv is invoked here (not at import time) to avoid side-effects on import.
    """
    load_dotenv(override=True)
    e = _get_env(env)

    # Top-level
    service_name = e.get("SERVICE_NAME", "ConvFinQA_ChatApp")
    prometheus_port = _get_int(e.get("PROMETHEUS_PORT", "9443"), 9443)    
    logging_level = e.get("LOGGING_LEVEL", "INFO").upper()
    max_workers = _get_int(e.get("MAX_WORKERS", "8"), 8)
    mistral_api_key = e.get("MISTRAL_API_KEY", "")

    # Weaviate config
    weaviate_config = WeaviateConfig(            
        http_host=e.get("WEAVIATE_HTTP_HOST", "localhost"),
        http_port=_get_int(e.get("WEAVIATE_HTTP_PORT", "8080"), 8080),
        http_secure=e.get("WEAVIATE_HTTP_SECURE", "false").lower() == "true",
        grpc_host=e.get("WEAVIATE_GRPC_HOST", "localhost"),
        grpc_port=_get_int(e.get("WEAVIATE_GRPC_PORT", "8080"), 8080),
        grpc_secure=e.get("WEAVIATE_GRPC_SECURE", "false").lower() == "true",
        api_key=e.get("WEAVIATE_API_KEY", ""),
        weaviate_version=e.get("WEAVIATE_VERSION", "1.19.3"),
    )

    # LLM config
    llm_config = _build_llm_config(e)

    max_chat_tokens = _get_int(e.get("MAX_CHAT_TOKENS", "64000"), 64_000)

    return Config(
        service_name=service_name,
        prometheus_port=prometheus_port,
        logging_level=logging_level,
        max_workers=max_workers,
        llm_config=llm_config,
        weaviate=weaviate_config,
        embeddings_config=_build_azure_embedding_config(e),
        mistral_api_key=mistral_api_key,
        max_chat_tokens=max_chat_tokens if max_chat_tokens >= 20000 else 20000
    )

CONFIG = load_config()