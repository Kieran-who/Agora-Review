from agent.workers.persona_generator import PersonaGeneratorAgent    
from agent.workers.participant import Participant
from agent.master import OrganiserAgent
from ai.models import LMMRequest, ChatMessage
from ai.client import get_llm_provider
from utils.tool_parser import extract_output_text
from utils.pdf_to_markdown import convert_pdf_to_md
from utils.sanitise_names import sanitize_filename
from config import CONFIG
import os
import sys
from pathlib import Path
from mistralai import Mistral

def main():

    files_to_process: list[str] = [] 
    
    file_path = sys.argv[1] if len(sys.argv) > 1 else None

    if not file_path or os.path.isfile(file_path):
        # If no file path we look for all pdfs in the current directory
        for f in os.listdir(Path(__file__).resolve().parent.parent):
            if f.lower().endswith('.pdf'):
                files_to_process.append(f)
    else:
        if not file_path.lower().endswith('.pdf'):
            raise ValueError(f"File {file_path} is not a PDF")
        files_to_process.append(file_path)    
    
    mistral_client = Mistral(api_key=CONFIG.mistral_api_key)

    for file_path in files_to_process:

        content = convert_pdf_to_md(mistral_client, get_llm_provider(), file_path)

        if not content or len(content) < 100:
            raise ValueError("Failed to extract content from PDF or content too short")

        # Generate personas
        persona_agent = PersonaGeneratorAgent()
        personas = persona_agent.proceed(content)

        participants: list[Participant] = []

        bios = ""

        for i in personas:
            bios += f"Name: {i.name}\n\nBio:\n\n{i.persona}\n\n---\n\n"

        if len(bios) < 100 or len(personas) == 0:
            raise ValueError("Generated bios too short")

        for i in personas:
            participant = Participant(persona=i, bios=bios, paper=content)
            participants.append(participant)

        # Get topic
        request = LMMRequest(
            model_size='small',
            messages=[
                ChatMessage(role="user", content=f"Provide a short title for a roundtable discussion based on the following paper. Return just one and only the text:\n\n---\n\n{content}")
            ],
            tool_calls=[],
            use_grounding=False,
            max_tokens=50,
            temperature=0.8
        )
        result = get_llm_provider().generate_openAI_completion(request)

        topic = extract_output_text(result)
        if not topic:
            raise ValueError("No topic generated")

        # Sanitize topic for filename
        topic = sanitize_filename(topic)

        host = OrganiserAgent(participants=participants, topic=topic.replace("Roundtable: ", "").strip(), paper=content, bios=bios)

        host.host_roundtable()

        # Finally, move the PDF file into the processed folder
        processed_folder = Path(__file__).resolve().parent.parent / "processed"
        processed_folder.mkdir(exist_ok=True)
        os.rename(file_path, processed_folder / Path(file_path).name)

if __name__ == "__main__":
    main()