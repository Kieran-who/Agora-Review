from dataclasses import dataclass
from typing import Optional

@dataclass
class AzureEmbeddingProviderConfig:
    resource_name: str
    deployment_name: str
    api_version: str = "2023-05-15"    
    api_key: Optional[str] = None
    max_text_tokens: int = 8191
    vector_length: int = 1536 # default for text-embedding-3-small

@dataclass(slots=True)
class EmbeddingRequest:
    text: str
    max_text_tokens: int

@dataclass(slots=True)
class EmbeddingUsage:
    prompt_tokens: int
    total_tokens: int

@dataclass(slots=True)
class EmbeddingResponse:
    embedding: list[float]
    usage: EmbeddingUsage
    model_used: str
    provider: str

class EmbeddingError(RuntimeError):
    pass