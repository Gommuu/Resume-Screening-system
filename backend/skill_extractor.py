import re

SKILL_LIST = [

    # Programming Languages
    "python",
    "java",
    "c",
    "c++",
    "c#",
    "javascript",
    "typescript",
    "php",
    "ruby",
    "go",
    "rust",
    "swift",
    "kotlin",
    "r",

    # Frontend
    "html",
    "css",
    "react",
    "angular",
    "vue",
    "next.js",
    "bootstrap",
    "tailwind css",
    "jquery",

    # Backend
    "node.js",
    "express",
    "flask",
    "django",
    "fastapi",
    "spring",
    "spring boot",
    "laravel",

    # Database
    "sql",
    "mysql",
    "postgresql",
    "mongodb",
    "sqlite",
    "oracle",
    "redis",
    "firebase",

    # Cloud
    "aws",
    "azure",
    "gcp",

    # DevOps
    "docker",
    "kubernetes",
    "jenkins",
    "git",
    "github",
    "gitlab",

    # AI / ML
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "nlp",
    "computer vision",
    "tensorflow",
    "keras",
    "pytorch",
    "scikit-learn",
    "opencv",

    # Data Science
    "numpy",
    "pandas",
    "matplotlib",
    "seaborn",

    # Analytics
    "power bi",
    "tableau",
    "excel",

    # CS Fundamentals
    "data structures",
    "algorithms",
    "oop",
    "operating system",
    "computer networks",
    "dbms",

    # APIs
    "rest api",
    "graphql",

    # Mobile
    "android",
    "flutter",
    "react native",

    # Testing
    "selenium",
    "pytest",
    "junit",

    # HR
    "recruitment",
    "communication",
    "leadership",
    "management",
    "hrms",
    "employee relations",

    # Other
    "linux",
    "agile",
    "scrum",
    "problem solving"

]


def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in SKILL_LIST:

        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, text):

            found_skills.append(skill)

    return sorted(list(set(found_skills)))


from backend.resume_parser import extract_text_from_pdf
from backend.preprocessing import clean_text


if __name__ == "__main__":

    raw_text = extract_text_from_pdf("../dataset/R4.pdf")

    cleaned = clean_text(raw_text)

    skills_found = extract_skills(cleaned)

    print(skills_found)