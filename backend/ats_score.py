from backend.preprocessing import preprocess_text


def calculate_ats_score(resume_text, similarity_score, matched_skills, required_skills):
    """
    Calculate ATS Score out of 100
    """

    resume_text = preprocess_text(resume_text)

    score = 0

    # -----------------------------
    # 1. Similarity Score (50 Marks)
    # -----------------------------
    score += (similarity_score / 100) * 50

    # -----------------------------
    # 2. Skill Match (30 Marks)
    # -----------------------------
    if len(required_skills) > 0:
        skill_percentage = (len(matched_skills) / len(required_skills)) * 100
        score += (skill_percentage / 100) * 30

    # -----------------------------
    # 3. Education Section (10 Marks)
    # -----------------------------
    education_keywords = [
        "education",
        "b.tech",
        "btech",
        "b.e",
        "m.tech",
        "mtech",
        "degree",
        "university"
    ]

    if any(word in resume_text for word in education_keywords):
        score += 10

    # -----------------------------
    # 4. Experience Section (10 Marks)
    # -----------------------------
    experience_keywords = [
        "experience",
        "internship",
        "work",
        "employment"
    ]

    if any(word in resume_text for word in experience_keywords):
        score += 10

    return round(score, 2)


# -----------------------------
# Testing
# -----------------------------

if __name__ == "__main__":

    resume = """
    Education
    B.Tech Computer Science

    Skills
    Python SQL Flask Git Machine Learning

    Experience
    Python Developer Intern
    """

    similarity = 82

    matched_skills = [
        "python",
        "sql",
        "flask",
        "git"
    ]

    required_skills = [
        "python",
        "sql",
        "flask",
        "git",
        "docker"
    ]

    ats = calculate_ats_score(
        resume,
        similarity,
        matched_skills,
        required_skills
    )

    print("ATS Score :", ats)