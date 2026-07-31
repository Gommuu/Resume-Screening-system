from backend.preprocessing import preprocess_text


def generate_recommendations(
    resume_text,
    matched_skills,
    required_skills,
    ats_score
):

    resume_text = preprocess_text(resume_text)

    recommendations = []

    # -----------------------------
    # Missing Skills
    # -----------------------------
    missing_skills = []

    for skill in required_skills:
        if skill not in matched_skills:
            missing_skills.append(skill)

    if missing_skills:
        recommendations.append(
            "Add missing skills: " + ", ".join(missing_skills)
        )

    # -----------------------------
    # Projects Section
    # -----------------------------
    if "project" not in resume_text:
        recommendations.append(
            "Add a Projects section."
        )

    # -----------------------------
    # Certifications
    # -----------------------------
    if "certification" not in resume_text:
        recommendations.append(
            "Add Certifications."
        )

    # -----------------------------
    # Experience
    # -----------------------------
    if "experience" not in resume_text:
        recommendations.append(
            "Include Work Experience or Internship."
        )

    # -----------------------------
    # ATS Score
    # -----------------------------
    if ats_score < 70:
        recommendations.append(
            "Improve keyword matching with the Job Description."
        )

    return recommendations


# -----------------------------
# Testing
# -----------------------------
if __name__ == "__main__":

    resume = """
    Education
    B.Tech Computer Science

    Skills
    Python SQL Flask Git
    """

    matched = [
        "python",
        "sql",
        "flask"
    ]

    required = [
        "python",
        "sql",
        "flask",
        "docker",
        "kubernetes"
    ]

    ats = 65

    tips = generate_recommendations(
        resume,
        matched,
        required,
        ats
    )

    for tip in tips:
        print("-", tip)