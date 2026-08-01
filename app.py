from flask import Flask, request, jsonify
import os
from flask_cors import CORS

from backend.contact_extractor import extract_name, extract_email, extract_phone
from backend.resume_parser import extract_text_from_pdf, extract_text_from_docx
from backend.preprocessing import clean_text
from backend.skill_extractor import extract_skills
from backend.similarity import calculate_similarity
from backend.ats_score import calculate_ats_score
from backend.recommendation import get_recommendation

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return "AI Resume Screening Backend is Running!"

JOB_DESCRIPTION = """
Looking for a Python Developer with SQL, Flask, Git,
Machine Learning and Docker experience.
"""

REQUIRED_SKILLS = [
    "python",
    "sql",
    "flask",
    "git",
    "machine learning",
    "docker"
]

@app.route("/upload", methods=["POST"])
def upload_resume():
    file = request.files["resume"]
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    filename = file.filename

    if filename.lower().endswith(".pdf"):
        raw_text = extract_text_from_pdf(filepath)
    elif filename.lower().endswith(".docx"):
        raw_text = extract_text_from_docx(filepath)
    else:
        return jsonify({"error": "Unsupported file type. Please upload PDF or DOCX."}), 400
    name = extract_name(raw_text)
    email = extract_email(raw_text)
    phone = extract_phone(raw_text)
    cleaned_text = clean_text(raw_text)

    skills = extract_skills(cleaned_text)
    missing_skills = [s for s in REQUIRED_SKILLS if s not in skills]

    similarity = calculate_similarity(cleaned_text, JOB_DESCRIPTION)
    ats = calculate_ats_score(skills, REQUIRED_SKILLS)
    recommendation = get_recommendation(ats)

    return jsonify({
        "skills_found": skills,
        "name": name,
        "email": email,
        "phone": phone,
        "missing_skills": missing_skills,
        "similarity_score": round(similarity * 100, 2),
        "ats_score": ats,
        "recommendation": recommendation
    })

if __name__ == "__main__":
    app.run(debug=True)