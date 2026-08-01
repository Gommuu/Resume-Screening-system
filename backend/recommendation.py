def get_recommendation(score):
    if score > 85:
        return "Suitable Candidate"
    elif score >= 70:
        return "Consider Interview"
    elif score >= 50:
        return "Needs Improvement"
    else:
        return "Not Recommended"
    #test

from resume_parser import extract_text_from_pdf
from preprocessing import clean_text
from skill_extractor import extract_skills
from ats_score import calculate_ats_score

if __name__ == "__main__":
    raw_text = extract_text_from_pdf("../dataset/R4.pdf")
    cleaned = clean_text(raw_text)
    found_skills = extract_skills(cleaned)

    required_skills = ["python", "machine learning", "sql", "docker", "aws", "power bi"]
    score = calculate_ats_score(found_skills, required_skills)

    result = get_recommendation(score)
    print("ATS Score:", score)
    print("Recommendation:", result)