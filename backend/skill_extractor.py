SKILL_LIST = ["python",
    "typescript",
    "javascript",
    "c",
    "java",
    "php",
    "mysql",
    "node.js"]
def extract_skills(text):
    found_skills = []
    for skills in SKILL_LIST:
        if skills in text:
            found_skills.append(skills)
    return found_skills