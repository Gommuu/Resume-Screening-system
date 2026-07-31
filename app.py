from flask import Flask, request, jsonify
import os

from backend.resume_parser import extract_text_from_pdf
from backend.skill_extractor import extract_skills
from backend.similarity import calculate_similarity
from backend.ats_score import calculate_ats_score
from backend.recommendation import generate_recommendations

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return "AI Resume Screening Backend is Running!"

# Example Job Description
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

    # Resume Text
    resume_text = extract_text_from_pdf(filepath)

    # Skills
    skills = extract_skills(resume_text)

    # Similarity
    similarity = calculate_similarity(
        resume_text,
        JOB_DESCRIPTION
    )

    # ATS Score
    ats = calculate_ats_score(
        resume_text,
        similarity,
        skills,
        REQUIRED_SKILLS
    )

    # Recommendations
    tips = generate_recommendations(
        resume_text,
        skills,
        REQUIRED_SKILLS,
        ats
    )

    return jsonify({

        "skills": skills,

        "similarity": similarity,

        "ats_score": ats,

        "recommendations": tips

    })


if __name__ == "__main__":
    app.run(debug=True)