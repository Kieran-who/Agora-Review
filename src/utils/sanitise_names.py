import os
import re

def sanitize_filename(filename: str) -> str:
    base_name = os.path.splitext(filename)[0]
    extension = os.path.splitext(filename)[1].lower()

    clean_name = re.sub(r'[\\/*:?"<>|]', '_', base_name)    
    clean_name = re.sub(r'_+', '_', clean_name)
    clean_name = clean_name.strip('. ')

    if len(clean_name) > 240:
        clean_name = clean_name[:240]

    return clean_name + extension
