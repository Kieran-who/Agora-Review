from __future__ import annotations

import json
from dataclasses import dataclass
from typing import List

from openai.types.responses.response import Response

__all__ = ["ToolCallEvent", "extract_tool_calls", "extract_output_text"]

@dataclass
class ToolCallEvent:
    id: str
    name: str
    arguments_json: str

def extract_tool_calls(resp: Response) -> List[ToolCallEvent]:
    calls: List[ToolCallEvent] = []

    # Path A: top-level function_call items
    for out in getattr(resp, "output", []) or []:
        otype = getattr(out, "type", None)
        if otype == "function_call":
            name = getattr(out, "name", "") or ""
            call_id = getattr(out, "call_id", "") or getattr(out, "id", "") or ""
            raw_args = getattr(out, "arguments", None)
            if not name:
                continue
            if raw_args is None:
                args_json = "{}"
            elif isinstance(raw_args, (dict, list)):
                args_json = json.dumps(raw_args)
            else:
                try:
                    json.loads(str(raw_args))
                    args_json = str(raw_args)
                except Exception:
                    args_json = json.dumps({"value": str(raw_args)})
            if not call_id:
                call_id = f"call_{abs(hash(name + args_json)) % (10**12)}"
            calls.append(ToolCallEvent(id=str(call_id), name=name, arguments_json=args_json))

    # Path B: embedded inside message content
    for out in getattr(resp, "output", []) or []:
        if getattr(out, "type", None) != "message":
            continue
        for content in getattr(out, "content", []) or []:
            ctype = getattr(content, "type", None)
            if ctype in {"tool_call", "tool_use", "function_call"}:
                name = getattr(content, "name", None) or getattr(content, "function_name", None) or ""
                raw_args = getattr(content, "arguments", None) or getattr(content, "input", None)
                if not name:
                    continue
                if raw_args is None:
                    args_json = "{}"
                elif isinstance(raw_args, (dict, list)):
                    args_json = json.dumps(raw_args)
                else:
                    try:
                        json.loads(str(raw_args))
                        args_json = str(raw_args)
                    except Exception:
                        args_json = json.dumps({"value": str(raw_args)})
                call_id = getattr(content, "id", None) or getattr(content, "call_id", None)
                if not call_id:
                    call_id = f"call_{abs(hash(name + args_json)) % (10**12)}"
                calls.append(ToolCallEvent(id=str(call_id), name=name, arguments_json=args_json))

    return calls

def extract_output_text(resp: Response) -> str:
    txt = getattr(resp, "output_text", None)
    if isinstance(txt, str):
        return txt
    chunks: List[str] = []
    for out in getattr(resp, "output", []) or []:
        if getattr(out, "type", None) != "message":
            continue
        for content in getattr(out, "content", []) or []:
            if getattr(content, "type", None) == "output_text":
                chunks.append(getattr(content, "text", "") or "")
    return "".join(chunks)