def get_recommendation(score):
    """
    Generate recommendation based on ATS Score.
    """

    if score >= 90:
        return "Excellent Match - Highly Recommended"

    elif score >= 80:
        return "Strong Candidate - Recommended"

    elif score >= 70:
        return "Good Candidate - Consider for Interview"

    elif score >= 60:
        return "Average Match - Needs Skill Improvement"

    elif score >= 40:
        return "Below Average - Significant Skill Gap"

    else:
        return "Not Recommended"


# ================= TEST =================

from backend.resume_parser import extract_text_from_pdf
from backend.preprocessing import clean_text
from backend.skill_extractor import extract_skills
from backend.ats_score import calculate_ats_score

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

    recommendation = get_recommendation(score)

    print("Skills Found :", found_skills)
    print("ATS Score :", score)
    print("Recommendation :", recommendation)