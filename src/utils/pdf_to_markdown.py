import base64
from pydantic import BaseModel
import json
from ai.client import LLMProvider
from ai.models import LMMRequest, ChatMessage, FunctionToolParam
from utils.tool_parser import extract_tool_calls, extract_output_text
from mistralai import Mistral
from openai.types.responses.response_input_image_param import ResponseInputImageParam
from openai.types.responses import ResponseInputMessageContentListParam

def encode_pdf(pdf_path: str):
    """Encode the pdf to base64."""
    try:
        with open(pdf_path, "rb") as pdf_file:
            return base64.b64encode(pdf_file.read()).decode('utf-8')
    except FileNotFoundError:
        print(f"Error: The file {pdf_path} was not found.")
        return None
    except Exception as e:  # Added general exception handling
        print(f"Error: {e}")
        return None

class ExtractedMarkdown(BaseModel):
    description: str

class ContentClassification(BaseModel):
    classification: bool

def check_img_worth_keeping(openAI_client: LLMProvider, base64_string: str) -> bool:
    """Simple LLM call to determine if the image is worth keeping. 
    For example we will exclude logos, placeholders or purely decorative images."""
    # This is a placeholder implementation. You can customize the description as needed.
    message_content: ResponseInputMessageContentListParam = [
        ResponseInputImageParam(
                detail="high",
                type="input_image",
                image_url=base64_string)
    ]

    user_message = ChatMessage(
        role="user",
        content=message_content      
    )
    
    send_messages: list[ChatMessage] = [
        ChatMessage(
            role="user",
            content="Your role is to classify whether this image has meaningful content or not. For example, logos, decorative images or placeholders are not meaningful, all other images, such as diagrams, tables and other images with content are meaningful. Return true if the image is meaningful, false otherwise. You must return your response using valid JSON."
        ),
        user_message
    ]

    request = LMMRequest(
        model_size="small",
        messages=send_messages,
        tool_calls=[FunctionToolParam(
                name="assess_image",
                description="Call this function to assess the content of the image.",
                type="function",
                parameters={
                        "type": "object",
                        "properties": {
                            "meaningful_content": {
                                "type": "boolean",
                                "description": "Whether the image contains meaningful content or not. True if it does, false otherwise.",
                            },                            
                         },
                         "required": ["meaningful_content"],
                         "additionalProperties": False
                    },
                strict=True
            )],
        max_tokens=100,
        require_tool_use=True,
    )

    response = openAI_client.generate_openAI_completion(request)
    result = extract_tool_calls(response)
    if not result:
        print(f"Failed to extract tool calls from response: {response}")
        return False
    
    try:
        fn_args = json.loads(result[0].arguments_json)
        if not fn_args.get("meaningful_content"):
            raise ValueError("No assessment generated")
        return fn_args.get("meaningful_content")
    except:
        return False

def get_img_description(openAI_client: LLMProvider, base64_string: str):
    """Generate a description for the image based on its base64 string."""
    # This is a placeholder implementation. You can customize the description as needed.
    message_content: ResponseInputMessageContentListParam = [
        ResponseInputImageParam(
                detail="high",
                type="input_image",
                image_url=base64_string)
    ]

    user_message = ChatMessage(
        role="user",
        content=message_content      
    )

    send_messages = [
        ChatMessage(
            role="user",
            content="Your role is to describe this image so that it can be read by an accessibility screen reader. The text you return is being used in an accessibility context so it's vital you provide a highly detailed and descriptive account of the image and its content. Return the image description only."
        ),
        user_message
    ]
    request = LMMRequest(
        model_size="small",
        messages=send_messages,
        tool_calls=[],
        max_tokens=300,
        require_tool_use=False,
    )

    response = openAI_client.generate_openAI_completion(request)
    text = extract_output_text(response)
    if not text:
        print(f"Failed to extract text from response: {response}")
        return ""

    return text

def convert_pdf_to_md(mistral_client: Mistral, openAI_client: LLMProvider, pdf_path: str):
    """Convert the PDF to Markdown."""

    base64_pdf = encode_pdf(pdf_path)
    if not base64_pdf:
        print(f"Failed to encode PDF: {pdf_path}. Skipping.")
        return

    ocr_response = mistral_client.ocr.process(
        model="mistral-ocr-latest",
        include_image_base64=True,
        document={
            "type": "document_url",
            "document_url": f"data:application/pdf;base64,{base64_pdf}"
        }
    )
    combined_md = ''
    index = 1
    for p in ocr_response.pages:
        combined_md += p.markdown
        combined_md += f'\n\n> <p style="text-align: center;">~ page {index} ~</p>\n\n'
        index += 1
        if p.images and len(p.images) > 0:
            
            for img in p.images:
                if img.image_base64 is None:
                    continue
                img_data_string = img.image_base64
                img_name = img.id                 
            
                # We check whether the image is meaningful
                check = check_img_worth_keeping(openAI_client, str(img_data_string))
                if not check:
                    combined_md = combined_md.replace(f'![{img_name}]({img_name})', '')
                else:                                
                    description = get_img_description(openAI_client, str(img_data_string))                    
                    combined_md = combined_md.replace(f'![{img_name}]', f'![{description}]')                
            
    combined_md = combined_md.replace("(img-", "(imgs/img-")
    
    return combined_md