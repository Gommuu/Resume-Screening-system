def calculate_ats_score(found_skills, required_skills):
    if not required_skills:
        return 0 
    matched = [skill for skill in required_skills if skill in found_skills]
    score = (len(matched) / len(required_skills)) * 100
    return round(score, 2)

##TESTS
from resume_parser import extract_text_from_pdf
from preprocessing import clean_text
from skill_extractor import extract_skills

if __name__ == "__main__":
    raw_text = extract_text_from_pdf("../dataset/R4.pdf")
    cleaned = clean_text(raw_text)
    found_skills = extract_skills(cleaned)
    required_skills = ["python", "machine learning", "sql", "docker", "aws", "power bi"]

    score = calculate_ats_score(found_skills, required_skills)
    print("Skills Found:", found_skills)
    print("ATS Score:", score)

        



