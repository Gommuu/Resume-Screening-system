import re

def preprocess_text(text):
    text = text.lower()                 # lowercase
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # punctuation remove
    text = re.sub(r'\s+', ' ', text).strip()    # extra spaces remove
    return text