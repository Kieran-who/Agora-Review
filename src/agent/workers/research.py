from pathlib import Path
from ai.client import get_llm_provider
from ai.models import LMMRequest, ChatMessage
from openai.types.responses.function_tool_param import FunctionToolParam
from agent.tools import ToolSpec, BoundTools

PROMPT_FILE_NAME = "research.txt"

class ResearchAgent:
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
            ToolSpec("get_recent_news", "Get news articles over previous 24 hours based on a provided search string.", 
                     {
                         "type": "object", 
                         "properties": {
                             "query": {"type": "string"}
                        }, 
                        "required": ["query"], 
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

    def proceed(self, query: str) -> str | None:
        bound = self._get_tools()
        tools = bound.function_params
        request = LMMRequest(
            model_size="large",
            messages=[                
                ChatMessage(role="user", content=self.prompt.replace("|query|", query))
            ],
            tool_calls=tools,
            use_grounding=True,
            max_tokens=50000,
            temperature=0.7
        )
        response = self.llm_provider.generate_google_completion(request)
        print(response)
        return response.text