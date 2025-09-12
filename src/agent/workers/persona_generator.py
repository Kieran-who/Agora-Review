from pathlib import Path
from dataclasses import dataclass
from ai.client import get_llm_provider
from ai.models import LMMRequest, ChatMessage
from utils.tool_parser import extract_tool_calls
from openai.types.responses.function_tool_param import FunctionToolParam
from agent.tools import ToolSpec, BoundTools
import json

PROMPT_FILE_NAME = "persona_generator.txt"

@dataclass(frozen=True)
class PersonaItem:
    persona: str
    name: str

class PersonaGeneratorAgent:
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
    
    def _get_tools(self) -> BoundTools:        
        specs: list[ToolSpec] = [
            ToolSpec("store_personas", "Call this function to store the list of personas you have generated.", 
                     {
                        "type": "object",
                        "properties": {
                            "personas": {
                                "type": "array", 
                                "description": "An array of personas.",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "bio": {
                                            "type": "string",
                                            "description": "A detailed bio of the person, their research interests and their theoretical and philosophical viewpoints as relevant to the article."
                                        },
                                        "name": {
                                            "type": "string",
                                            "description": "The name of the person including their title."
                                        }
                                    },
                                    "additionalProperties": False,
                                    "required": ["bio", "name"],
                                },
                            },
                         },
                         "required": ["personas"],
                         "additionalProperties": False
                    }),
        ]

        return BoundTools(
            function_params=[FunctionToolParam(
            name=s.name,
            description=s.description,
            type="function",
            parameters=s.schema,
            strict=True,
        ) for s in specs]
        )
        
    def proceed(self, article_content: str) -> list[PersonaItem]:    
        bound = self._get_tools()
        tools = bound.function_params    
        request = LMMRequest(
            model_size="large",
            messages=[
                ChatMessage(role="user", content=f"{self.prompt}\n---\n{'#' * 10} ARTICLE {'#' * 10}\n{article_content}")
            ],
            tool_calls=tools,
            use_grounding=False,
            max_tokens=100000,
            temperature=0.8,
            require_tool_use=True
        )
        response = self.llm_provider.generate_openAI_completion(request)
        persona_details = extract_tool_calls(response)
        p_list = json.loads(persona_details[0].arguments_json)
        
        return [PersonaItem(persona=p['bio'], name=p['name']) for p in p_list.get("personas", [])]