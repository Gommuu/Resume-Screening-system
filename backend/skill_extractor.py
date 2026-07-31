from preprocessing import preprocess_text

SKILLS = [
    "python",
    "java",
    "c++",
    "sql",
    "mysql",
    "mongodb",
    "html",
    "css",
    "javascript",
    "react",
    "nodejs",
    "django",
    "flask",
    "machine learning",
    "deep learning",
    "tensorflow",
    "pytorch",
    "pandas",
    "numpy",
    "git"
]


def extract_skills(text):

    text = preprocess_text(text)

    found_skills = []

    for skill in SKILLS:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))

if __name__ == "__main__":
    sample = """
    I know Python, SQL, Machine Learning, Pandas and Git.
    """

    skills = extract_skills(sample)

    print(skills)