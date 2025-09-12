from pathlib import Path
from ai.client import get_llm_provider
from ai.models import LMMRequest, ChatMessage

PROMPT_FILE_NAME = "writer.txt"

class WriterAgent:
    def __init__(self):
        self.llm_provider = get_llm_provider()
        self.prompt = self._get_prompt()    

    def _get_prompt(self) -> str:
        # Resolve prompts/research.txt relative to this file or project root
        start = Path(__file__).resolve().parent
        for base in [start, *start.parents, Path.cwd()]:
            candidate = base / "prompts" / PROMPT_FILE_NAME
            if candidate.is_file():
                return candidate.read_text(encoding="utf-8")
        raise FileNotFoundError(f"Could not find prompts/{PROMPT_FILE_NAME} starting from {start}")
    
    def proceed(self, paper: str, transcript: str, bios: str) -> str | None:
        request = LMMRequest(
            model_size="large",
            messages=[                
                ChatMessage(role="user", content=self.prompt.replace("|paper|", paper).replace("|paper|", transcript).replace('|bios|', bios))
            ],
            tool_calls=[],
            use_grounding=False,
            max_tokens=100000,
            temperature=0.85
        )
        response = self.llm_provider.generate_google_completion(request)
        
        return response.text