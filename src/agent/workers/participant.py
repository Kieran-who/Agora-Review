from pathlib import Path
from ai.client import get_llm_provider
from ai.models import LMMRequest, ChatMessage
from utils.tool_parser import extract_output_text
from agent.workers.persona_generator import PersonaItem

PROMPT_FILE_NAME = "participant.txt"

class Participant:
    def __init__(self, persona: PersonaItem, bios: str, paper: str,):
        self.llm_provider = get_llm_provider()
        self.persona = persona
        self.prompt = self._get_prompt().replace('|PAPER|', paper).replace('|BIOS|', bios)

    def _get_prompt(self) -> str:
        # Resolve prompts/research.txt relative to this file or project root
        start = Path(__file__).resolve().parent
        for base in [start, *start.parents, Path.cwd()]:
            candidate = base / "prompts" / PROMPT_FILE_NAME
            if candidate.is_file():
                text = candidate.read_text(encoding="utf-8")
                return text.replace("|PERSONA|", self.persona.persona).replace("|NAME|", self.persona.name)
        raise FileNotFoundError(f"Could not find prompts/{PROMPT_FILE_NAME} starting from {start}")
    
    def proceed(self, transcript: str,  nudge: str) -> str:
        request = LMMRequest(
            model_size="large",
            messages=[
                ChatMessage(role="user", content=f"{self.prompt.replace('|TRANSCRIPT|', transcript).replace('|NUDGE|', nudge)}")
            ],
            tool_calls=[],
            use_grounding=False,
            max_tokens=100000,
            temperature=0.8
        )
        response = self.llm_provider.generate_openAI_completion(request)
        text = extract_output_text(response)
        
        return text