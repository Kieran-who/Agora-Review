from dataclasses import dataclass
from ai.client import get_llm_provider
from ai.models import LMMRequest, ChatMessage
from utils.tool_parser import extract_tool_calls
from utils.tokenizer import handle_token_request, TokenRequest
from utils.update_index_features import update_index_features
from openai.types.responses.function_tool_param import FunctionToolParam
from agent.tools import ToolSpec, BoundTools
from agent.workers.participant import Participant
from agent.workers.writer import WriterAgent
import json
import os
from pathlib import Path
from datetime import datetime

PROMPT_FILE_NAME = "host.txt"

@dataclass(frozen=True)
class TranscriptSegment:
    speaker: str
    text: str

class OrganiserAgent:
    def __init__(self, participants: list[Participant], topic: str, paper: str, bios: str):
        self.participants = participants
        self.llm_provider = get_llm_provider()
        self.transcript: list[TranscriptSegment] = []
        self.paper = paper
        self.topic = topic
        self.bios = bios
        self.prompt = self._get_prompt().replace('|PAPER|', paper).replace('|BIOS|', bios)
        self.parent_folder = Path(__file__).resolve().parent.parent.parent
        os.makedirs(f'{self.parent_folder}/content', exist_ok=True)
        os.makedirs(f'{self.parent_folder}/content/{self.topic}', exist_ok=True)

    def _get_prompt(self) -> str:
        # Resolve prompts/research.txt relative to this file or project root
        start = Path(__file__).resolve().parent
        for base in [start, *start.parents, Path.cwd()]:
            candidate = base / "prompts" / PROMPT_FILE_NAME
            if candidate.is_file():
                text = candidate.read_text(encoding="utf-8")
                return text
        raise FileNotFoundError(f"Could not find prompts/{PROMPT_FILE_NAME} starting from {start}")

    def _get_tools(self) -> BoundTools:
        specs: list[ToolSpec] = [
            ToolSpec("participant_prompt", "Call this function to prompt a participant to continue the roundtable discussion.", 
                     {
                        "type": "object",
                        "properties": {
                            "participant": {
                                "type": "string", 
                                "description": "The name of the participant (exactly how it appears in the bios after Name: ). You can only prompt one participant at a time and you can only prompt participants that are listed in the bios.",
                            },
                            "prompt": {
                                "type": "string", 
                                "description": "The prompt to provide to the participant to continue the discussion.",
                            },
                         },
                         "required": ["participant", "prompt"],
                         "additionalProperties": False
                    }),
            ToolSpec("finalize_roundtable", "Call this function to end the roundtable discussion.", 
                     {
                        "type": "object",
                        "properties": {
                            "concluding_remarks": {
                                "type": "string", 
                                "description": "Short concluding remarks to close the roundtable and summarise the key points discussed.",
                            },
                         },
                         "required": ["concluding_remarks"],
                         "additionalProperties": False
                    })
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
    
    def _get_transcript_text(self) -> str:
        return "\n\n---\n\n".join([f"### Speaker: {seg.speaker}\n\n{seg.text}" for seg in self.transcript])
    
    def _save_transcript(self):
        text = self._get_transcript_text()

        save_txt = f"""---
title: "{self.topic} - Transcript"
date: "{datetime.now().strftime('%Y-%m-%d')}"
prev: 
  text: See write up
  link: '/{self.topic}/summary.md'
next: false
---\n\n{text}"""
        with open(f'{self.parent_folder}/content/{self.topic}/transcript.md', 'w') as file:
            file.write(save_txt)

    def _write_summary(self):
        writing_agent = WriterAgent()
        summary = writing_agent.proceed(paper=self.paper, transcript=self._get_transcript_text(), bios=self.bios)

        metatdata = self._get_metadata(summary) if summary else ""

        md_content = f"{metatdata}\n\n{summary}" if summary else ""

        if summary:
            with open(f'{self.parent_folder}/content/{self.topic}/summary.md', 'w') as file:
                file.write(md_content)
    
    def _get_metadata(self, content: str) -> str:
        # Get topic
        request = LMMRequest(
            model_size='small',
            messages=[
                ChatMessage(role="user", content=f"Use the store_metadata function to store the required metadata based on this roundtable summary:\n\n---\n\n{content}")
            ],
            tool_calls=[FunctionToolParam(
                name="store_metadata",
                description="Call this function to store metadata about the roundtable discussion.",
                type="function",
                parameters={
                        "type": "object",
                        "properties": {
                            "content_tags": {
                                "type": "array",
                                "items": {
                                    "type": "string"
                                },
                                "description": "A list of up to three general tags to categorise the content of the roundtable discussion. Each tag should be a single word or short phrase (no more than 3 words).",
                            },
                            "outline":{
                                "type": "string",
                                "description": "One sentence summary teasing the content of the roundtable discussion.",
                            }
                         },
                         "required": ["content_tags", "outline"],
                         "additionalProperties": False
                    },
                strict=True
            )],
            use_grounding=False,
            max_tokens=150,
            temperature=0.8,
            require_tool_use=True
        )
        result = self.llm_provider.generate_openAI_completion(request)

        fn_details = extract_tool_calls(result)
        try:
            fn_args = json.loads(fn_details[0].arguments_json)
            if not fn_args.get("outline") or not fn_args.get("content_tags"):
                raise ValueError("No outline or content tags generated")
            # We can now update the index.md file to list the latest roundtable
            with open(f'{self.parent_folder}/content/index.md', 'r') as file:
                index_content = file.read()

            new_index_content = update_index_features(index_content, self.topic, fn_args.get("outline"), f'/{self.topic}/summary.md')

            with open(f'{self.parent_folder}/content/index.md', 'w') as file:
                file.write(new_index_content)
            # Return formatted front matter
            return f"""---
title: "{self.topic.replace('_', ':')}"
date: "{datetime.now().strftime('%Y-%m-%d')}"
outline: "{fn_args.get("outline")}"
tags: {", ".join(fn_args.get("content_tags", []))}
prev: false
next:
  text: See full transcript
  link: '/{self.topic}/transcript.md'
---"""
        except Exception as e:
            raise ValueError(f"Error extracting metadata: {e}")

    def host_roundtable(self):
        bound = self._get_tools()
        tools = bound.function_params  
        continue_roundtable = True
        counter = 0
        while continue_roundtable:

            counter += 1
            
            transcript_checked = handle_token_request(TokenRequest(text=self._get_transcript_text(), number=400000)) 

            print(f"{counter}: transcript length: {transcript_checked.number}")           

            if transcript_checked.number > 250000:
                self.transcript.append(TranscriptSegment(speaker="Time check", text="You have 15 minutes remaining. Please start to wrap up the discussion."))

            if transcript_checked.number > 375000:
                continue_roundtable = False
                self.transcript.append(TranscriptSegment(speaker="Time check", text="You are out of time. You must conclude the roundtable this turn."))            
            
            transcript = self._get_transcript_text()

            request_messages = [
                    ChatMessage(role="user", content=f"{self.prompt.replace('|TRANSCRIPT|', transcript if len(transcript.strip()) > 0 else 'The roundtable has just started. Introduce the topic and kick off the discussion with the participants.')}")
                ]
            
            request = LMMRequest(
                model_size="large",
                messages=request_messages,
                tool_calls=tools,
                use_grounding=False,
                max_tokens=400000,
                temperature=0.8,
                require_tool_use=True
            )            
            
            response = self.llm_provider.generate_openAI_completion(request)
            try: 
                
                fn_details = extract_tool_calls(response)
                
                fn_name = fn_details[0].name
                fn_args = json.loads(fn_details[0].arguments_json)

                if fn_name == "finalize_roundtable":
                    self.transcript.append(TranscriptSegment(speaker="Host", text=fn_args.get("concluding_remarks", "")))
                    
                    print("Roundtable concluded.")
                    
                    continue_roundtable = False
                elif fn_name == "participant_prompt":
                    participant_name = fn_args.get("participant", "")
                    prompt = fn_args.get("prompt", "")

                    self.transcript.append(TranscriptSegment(speaker="Host", text=prompt))
                    
                    participant = next((p for p in self.participants if p.persona.name == participant_name), None)
                    if participant:
                        participant_response = participant.proceed(transcript=self._get_transcript_text(), nudge=prompt)

                        if participant_response:
                            self.transcript.append(TranscriptSegment(speaker=participant_name, text=participant_response))
            except Exception as e:
                print(f"Error: {e}")
                continue            
            
            self._save_transcript()
        self._save_transcript()
        self._write_summary()
        return self._get_transcript_text()