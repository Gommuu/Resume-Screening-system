import re 
def clean_text(text):
    text = text.lower()
    text = text.replace("\n"," ")
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    text = text.strip()
    return text
from backend.resume_parser import extract_text_from_pdf
if __name__ == "__main__":
    raw_text = extract_text_from_pdf("../dataset/Resume.pdf")
    cleaned = clean_text(raw_text)
    print(cleaned)