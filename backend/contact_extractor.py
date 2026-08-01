import re

def extract_email(text):
    match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    if match:
        return match.group()
    return None

def extract_phone(text):
    match = re.search(r"(\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}", text)
    if match:
        return match.group()
    return None
def extract_name(raw_text):
    lines = raw_text.strip().split("\n")
    for line in lines:
        line = line.strip()
        if line:
            return line
    return None
from backend.resume_parser import extract_text_from_pdf

if __name__ == "__main__":
    raw_text = extract_text_from_pdf("dataset/R4.pdf")

    print("Name:", extract_name(raw_text))
    print("Email:", extract_email(raw_text))
    print("Phone:", extract_phone(raw_text))