from __future__ import annotations

from typing import Optional

from config import CONFIG
from embeddings.providers.azure import AzureEmbeddingProvider

from embeddings.models import EmbeddingRequest, EmbeddingResponse, EmbeddingError

from logger import get_logger

logger = get_logger(__name__)

_EmbeddingProvider: Optional[EmbeddingProvider] = None

class EmbeddingProvider:
    """
    Interface for calling the preset embedding provider.
    """

    def __init__(self):
        self._embedding_provider = self._get_embedding_provider()

    def _get_embedding_provider(self):
            
        cfg = CONFIG.embeddings_config
        if not cfg:
            raise EmbeddingError("Azure embedding config is missing despite provider being set.")
        return AzureEmbeddingProvider(cfg)                        

    def generate(self, request: EmbeddingRequest) -> EmbeddingResponse:
        """
        Generate embeddings for the given request.

        :param request: The embedding request containing the text to embed.
        :return: The embedding response containing the generated embeddings.
        """
        if not request.max_text_tokens:
            request.max_text_tokens = CONFIG.embeddings_config.max_text_tokens
            
        return self._embedding_provider.generate(request)

def get_embedding_provider() -> EmbeddingProvider:
    global _EmbeddingProvider
    if _EmbeddingProvider is None:
        _EmbeddingProvider = EmbeddingProvider()
    return _EmbeddingProvider

# Whipe the provider for testing
def reset_embedding_provider() -> None:
    global _EmbeddingProvider
    _EmbeddingProvider = None