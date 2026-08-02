from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import json

"""FOR REPORT IMPORTS"""
from backend.report_generator import generate_report
from flask import send_file
"""-----------------------------"""
from backend.contact_extractor import extract_name, extract_email, extract_phone
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

with open("database/companies.json") as f:
    COMPANIES = json.load(f)

@app.route("/")
def home():
    return "AI Resume Screening Backend is Running!"

@app.route("/analyze", methods=["POST"])
def analyze_resume():
    file = request.files["resume"]
    company = request.form.get("company", "")
    job_role = request.form.get("job_role", "")

    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    company_key = company.lower().replace(" ", "_")
    role_key = job_role.lower().replace(" ", "_")

    if company_key not in COMPANIES:
        return jsonify({"error": f"No data for company: {company}"}), 400
    if role_key not in COMPANIES[company_key]:
        return jsonify({"error": f"No data for role: {job_role} at {company}"}), 400

    required_skills = COMPANIES[company_key][role_key]

    raw_text = extract_resume_text(filepath)

    name = extract_name(raw_text)
    email = extract_email(raw_text)
    phone = extract_phone(raw_text)

    cleaned_text = clean_text(raw_text)
    skills = extract_skills(cleaned_text)

    matched_skills = [s for s in required_skills if s in skills]
    missing_skills = [s for s in required_skills if s not in skills]

    job_description = f"""
We are hiring a {job_role} at {company}. The ideal candidate should have strong 
experience and hands-on skills in {', '.join(required_skills)}. This role requires 
someone who can work independently, solve problems effectively, communicate clearly 
with team members, and contribute to real projects using these technologies. 
Candidates with relevant education, practical project experience, and a solid 
understanding of {', '.join(required_skills)} are strongly encouraged to apply. 
We value analytical thinking, adaptability, and a strong grasp of core skills 
required for the {job_role} position.
"""
    cleaned_job = clean_text(job_description)
    similarity = calculate_similarity(cleaned_text, cleaned_job)

    ats = calculate_ats_score(skills, required_skills)
    recommendation = get_recommendation(ats)


    report_filename = f"{name or 'candidate'}_report.pdf".replace(" ", "_")
    generate_report(
        filename=report_filename,
        name=name or "Unknown",
        email=email or "N/A",
        phone=phone or "N/A",
        company=company,
        job_role=job_role,
        ats_score=ats,
        resume_match=round(similarity * 100, 2),
        matched_skills=matched_skills,
        missing_skills=missing_skills,
        recommendation=recommendation,
    )


    return jsonify({
        "name": name,
        "email": email,
        "phone": phone,
        "ats_score": ats,
        "resume_match": round(similarity * 100, 2),
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "recommendation": recommendation,
        "message": f"Based on the requirements for {job_role} at {company}, this candidate scored {ats}%.",
        "report_url": f"/download-report/{report_filename}"
    })

#---------------------DOWNLAOD ROUTE FOR REPORT---------------------------------------------

@app.route("/download-report/<filename>")
def download_report(filename):
    return send_file(f"reports/{filename}", as_attachment=True)


#--------ROLES SELECION--------------
@app.route("/roles/<company>")
def get_roles(company):
    company_key = company.lower().replace(" ", "_")
    if company_key not in COMPANIES:
        return jsonify([])
    roles = list(COMPANIES[company_key].keys())
    return jsonify(roles)


if __name__ == "__main__":
    app.run(debug=True)