from agent.workers.persona_generator import PersonaGeneratorAgent    
from agent.workers.participant import Participant
from agent.master import OrganiserAgent
from ai.models import LMMRequest, ChatMessage
from ai.client import get_llm_provider
from utils.tool_parser import extract_output_text
from pathlib import Path

with open('/Users/kieran/Documents/blog_agents/test.md', 'r') as file:
    content = file.read()

# Pipeline

# Generate personas
persona_agent = PersonaGeneratorAgent()
personas = persona_agent.proceed(content)

participants: list[Participant] = []

bios = ""

for i in personas:
    bios += f"Name: {i.name}\n\nBio:\n\n{i.persona}\n\n---\n\n"

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

print(topic)
host = OrganiserAgent(participants=participants, topic=topic.replace("Roundtable: ", "").strip(), paper=content, bios=bios)

host.host_roundtable()

# We now want to update the index.md file to list the latest roundtable
content_parent = Path(__file__).resolve().parent.parent.parent
content_path = content_parent / 'content' 

