from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os

from backend.report_generator import generate_report
from backend.contact_extractor import (
    extract_name,
    extract_email,
    extract_phone,
)
from backend.resume_parser import extract_resume_text
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


@app.route("/analyze", methods=["POST"])
def analyze_resume():

    # ---------------- Upload ----------------

    if "resume" not in request.files:
        return jsonify({"error": "Resume not uploaded"}), 400

    file = request.files["resume"]

    job_description = request.form.get("job_description", "").strip()

    if job_description == "":
        return jsonify({"error": "Job Description is required"}), 400

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # ---------------- Resume Parsing ----------------

    raw_text = extract_resume_text(filepath)

    # ---------------- Contact Extraction ----------------

    name = extract_name(raw_text)
    email = extract_email(raw_text)
    phone = extract_phone(raw_text)

    # ---------------- Cleaning ----------------

    cleaned_resume = clean_text(raw_text)
    cleaned_job = clean_text(job_description)

    # ---------------- Skills ----------------

    resume_skills = extract_skills(cleaned_resume)
    required_skills = extract_skills(cleaned_job)

    matched_skills = [
        skill for skill in required_skills
        if skill in resume_skills
    ]

    missing_skills = [
        skill for skill in required_skills
        if skill not in resume_skills
    ]

    # ---------------- Similarity ----------------

    similarity = calculate_similarity(
        cleaned_resume,
        cleaned_job
    )

    # ---------------- ATS ----------------

    ats_score = calculate_ats_score(
        resume_skills,
        required_skills
    )

    # ---------------- Recommendation ----------------

    recommendation = get_recommendation(ats_score)

    # ---------------- PDF Report ----------------

    report_filename = (
        f"{(name or 'candidate').replace(' ', '_')}_report.pdf"
    )

    generate_report(
        filename=report_filename,
        name=name or "Unknown",
        email=email or "N/A",
        phone=phone or "N/A",
        company="Custom",
        job_role="Job Description",
        ats_score=ats_score,
        resume_match=round(similarity * 100, 2),
        matched_skills=matched_skills,
        missing_skills=missing_skills,
        recommendation=recommendation,
    )

    # ---------------- Response ----------------

    return jsonify({

        "name": name,

        "email": email,

        "phone": phone,

        "ats_score": ats_score,

        "resume_match": round(similarity * 100, 2),

        "matched_skills": matched_skills,

        "missing_skills": missing_skills,

        "recommendation": recommendation,

        "message": f"Candidate scored {ats_score}% based on the provided Job Description.",

        "report_url": f"/download-report/{report_filename}"

    })


@app.route("/download-report/<filename>")
def download_report(filename):
    return send_file(
        f"reports/{filename}",
        as_attachment=True
    )


if __name__ == "__main__":
    app.run(debug=True)