from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict

from openai.types.responses.function_tool_param import FunctionToolParam

JsonDict = Dict[str, Any]

@dataclass(frozen=True)
class ToolSpec:
    name: str
    description: str
    schema: JsonDict    

@dataclass
class BoundTools:
    function_params: list[FunctionToolParam]    