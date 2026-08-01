SKILL_LIST = [
    "python",
    "typescript",
    "javascript",
    "java",
    "php",
    "mysql",
    "node.js",
    "machine learning",
    "sql",
    "docker",
    "aws",
    "power bi",
    "react",
    "git"
]
def extract_skills(text):
    found_skills = []
    for skills in SKILL_LIST:
        if skills in text:
            found_skills.append(skills)
    return found_skills


from resume_parser import extract_text_from_pdf
from preprocessing import clean_text

if __name__ == "__main__":
    raw_text = extract_text_from_pdf("../dataset/R4.pdf")
    cleaned = clean_text(raw_text)
    skills_found = extract_skills(cleaned)
    print(skills_found)