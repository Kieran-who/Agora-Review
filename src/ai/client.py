from __future__ import annotations

from typing import Optional

from config import CONFIG
from ai.providers.azure_openAI import AzureLLMProvider
from ai.providers.google import GoogleLLMProvider

from ai.models import LMMRequest
from openai.types.responses.response import Response
from google.genai.types import GenerateContentResponse

from logger import get_logger

logger = get_logger(__name__)

_LLMProvider: Optional[LLMProvider] = None

class LLMProvider:
    """
    Interface for calling the preset LLM provider.
    """

    def __init__(self):
        self._LLM_provider_openAI: AzureLLMProvider = AzureLLMProvider(CONFIG.llm_config.configs.azure)
        self._LLM_provider_google: GoogleLLMProvider = GoogleLLMProvider(CONFIG.llm_config.configs.google)   

    def generate_openAI_completion(self, request: LMMRequest) -> Response:
        """
        Generate completions for the given request.

        :param request: The completion request containing the text to complete.
        :return: The completion response.
        """
        
        return self._LLM_provider_openAI.generate(request)

    def generate_google_completion(self, request: LMMRequest) -> GenerateContentResponse:
        """
        Generate completions for the given request.

        :param request: The completion request containing the text to complete.
        :return: The completion response.
        """
        
        return self._LLM_provider_google.generate(request)
    
    def return_underlying_openAI_client(self, provider: str) -> AzureLLMProvider:        
        return self._LLM_provider_openAI

    def return_underlying_google_client(self, provider: str) -> GoogleLLMProvider:
        return self._LLM_provider_google

def get_llm_provider() -> LLMProvider:
    global _LLMProvider
    if _LLMProvider is None:
        _LLMProvider = LLMProvider()
    return _LLMProvider

# Whipe the provider for testing
def reset_llm_provider() -> None:
    global _LLMProvider
    _LLMProvider = None