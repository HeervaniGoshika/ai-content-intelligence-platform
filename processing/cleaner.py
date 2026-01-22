import re

def clean(text):
    text = re.sub(r"\s+", " ", text)
    return text.strip()