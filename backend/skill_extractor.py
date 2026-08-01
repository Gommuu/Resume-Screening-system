import re

SKILL_LIST = [
    "python", "java", "c", "c++", "c#", "javascript", "typescript", "php", "ruby", "go", "rust", "swift", "kotlin", "r",
    "html", "css", "react", "angular", "vue", "next.js", "bootstrap", "tailwind css", "jquery",
    "node.js", "express", "flask", "django", "fastapi", "spring", "spring boot", "laravel",
    "sql", "mysql", "postgresql", "mongodb", "sqlite", "oracle", "redis", "firebase",
    "aws", "azure", "gcp",
    "docker", "kubernetes", "jenkins", "git", "github", "gitlab",
    "machine learning", "deep learning", "artificial intelligence", "nlp", "computer vision",
    "tensorflow", "keras", "pytorch", "scikit-learn", "opencv",
    "numpy", "pandas", "matplotlib", "seaborn",
    "power bi", "tableau", "excel",
    "data structures", "algorithms", "oop", "operating system", "computer networks", "dbms",
    "rest api", "graphql",
    "android", "flutter", "react native",
    "selenium", "pytest", "junit",
    "recruitment", "communication", "leadership", "management", "hrms", "employee relations",
    "linux", "agile", "scrum", "problem solving"
]

def extract_skills(text):
    text = text.lower()
    found_skills = []
    for skill in SKILL_LIST:
        pattern = r"\b" + re.escape(skill.lower()) + r"\b"
        if re.search(pattern, text):
            found_skills.append(skill)
    return sorted(list(set(found_skills)))