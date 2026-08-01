def calculate_ats_score(found_skills, required_skills):

    """
    Calculate ATS score based on matched skills.
    """

    if not required_skills:
        return 0

    found_skills = [skill.lower() for skill in found_skills]
    required_skills = [skill.lower() for skill in required_skills]

    matched_skills = []

    for skill in required_skills:

        if skill in found_skills:

            matched_skills.append(skill)

    matched_count = len(matched_skills)
    total_required = len(required_skills)

    score = (matched_count / total_required) * 100

    if score > 100:
        score = 100

    return round(score, 2)


# ================= TEST =================

from backend.resume_parser import extract_text_from_pdf
from backend.preprocessing import clean_text
from backend.skill_extractor import extract_skills

if __name__ == "__main__":

    raw_text = extract_text_from_pdf("../dataset/R4.pdf")

    cleaned = clean_text(raw_text)

    found_skills = extract_skills(cleaned)

    required_skills = [
        "python",
        "machine learning",
        "sql",
        "docker",
        "aws",
        "power bi"
    ]

    score = calculate_ats_score(
        found_skills,
        required_skills
    )

    print("Skills Found :", found_skills)
    print("Required Skills :", required_skills)
    print("Matched Skills :", [s for s in required_skills if s in found_skills])
    print("ATS Score :", score)