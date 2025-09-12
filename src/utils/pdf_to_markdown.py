import base64
import os
from config import CONFIG
from pydantic import BaseModel
import json
from ai.client import LLMProvider
from ai.models import LMMRequest, ChatMessage, ImgContent, FunctionToolParam
from utils.tool_parser import extract_tool_calls, extract_output_text

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
    user_message = ChatMessage(
        role="user",
        content=ImgContent(
            type="image_url",
            image_url={"url": base64_string}
        )
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
    user_message = ChatMessage(
        role="user",
        content=ImgContent(
            type="image_url",
            image_url={"url": base64_string}
        )
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

def convert_pdf_to_md(mistral_client, openAI_client, pdf_path, output_path, update_description=False, new_name=None):
    """Convert the PDF to Markdown."""
    
    output_file_name = new_name if new_name else pdf_path.split("/")[-1].replace(".pdf", "")
    
    os.makedirs(output_path, exist_ok=True)
    os.makedirs(f"{output_path}/{output_file_name}", exist_ok=True)
    file_name = f"{output_path}/{output_file_name}/{output_file_name}.md"

    # Check if file already exists and skip if so
    if os.path.exists(file_name):
        print(f"File {file_name} already exists. Skipping.")
        return

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
            os.makedirs(f"{output_path}/{output_file_name}/imgs", exist_ok=True)
            for img in p.images:
                if img.image_base64 is None:
                    continue
                img_data_string = img.image_base64
                img_name = img.id                 
    
                # For main descriptive usage
                usage = None             

                # We check whether the image is meaningful
                check, img_check_usage = check_img_worth_keeping(openAI_client, img_data_string)
                if not check['classification']:
                    combined_md = combined_md.replace(f'![{img_name}]({img_name})', '')
                else:                                
                    description, usage = get_img_description(openAI_client, img_data_string)

                    if update_description:
                        combined_md = combined_md.replace(f'![{img_name}]', f'![{description['description']}]')

                img_filename = f"{output_path}/{output_file_name}/imgs/{img_name}" if check['classification'] else f"{output_path}/{output_file_name}/imgs/_{img_name}"
                
                # 1. Check for and strip the Data URI prefix
                if ',' in img_data_string:
                    encoded_data = img_data_string.split(',', 1)[1]
                else:
                    # The string is already pure base64
                    encoded_data = img_data_string

                # 2. Decode the string and save the file
                try:
                    img_binary_data = base64.b64decode(encoded_data)                                
                    with open(img_filename, "wb") as f_img:
                        f_img.write(img_binary_data)
                except (base64.binascii.Error, TypeError) as e:
                    print(f"Could not decode or save image '{img_name}'. Error: {e}")

                # Save the description object as json
                json_obj = img.model_dump()                
                json_obj['img_check_usage'] = img_check_usage.model_dump()
                json_obj['ignored'] = not check['classification']
                if usage:
                    json_obj['usage'] = usage.model_dump()
                if check['classification'] and description:
                    json_obj['description'] = description['description']
                del json_obj['image_base64']
                del json_obj['image_annotation']
                with open(img_filename.replace('.jpeg', '.json'), "w") as f_desc:
                    json.dump(json_obj, f_desc, indent=4)
            
    combined_md = combined_md.replace("(img-", "(imgs/img-")
    with open(file_name, "w") as f:
        f.write(combined_md)
    return combined_md