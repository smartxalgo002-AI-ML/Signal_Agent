import json
import re

def parse_signal(file_path: str):

    with open(file_path, "r", encoding="utf-8") as file:
        raw = file.read()

    raw = raw.strip()
    raw = raw.replace("'", '"')
    raw = re.sub(r'([{,]\s*)(\w+)\s*:', r'\1"\2":', raw)
    raw = re.sub(r':\s*(\d{4}-\d{2}-\d{2}T[0-9:\.\-Z]+)', r': "\1"', raw)
    raw = raw.replace("undefined", "null")
    raw = re.sub(r',\s*([}\]])', r'\1', raw)

    return json.loads(raw)
