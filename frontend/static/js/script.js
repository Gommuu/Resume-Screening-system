// ==========================
// DOM Elements
// ==========================

const atsStatus = document.getElementById("atsStatus");
const matchStatus = document.getElementById("matchStatus");
const skillOverview = document.getElementById("skillOverview");

const uploadInput = document.getElementById("resumeUpload");
const resumeName = document.getElementById("resumeName");
const resumeSize = document.getElementById("resumeSize");

const analyzeBtn = document.getElementById("analyzeBtn");
const downloadBtn = document.getElementById("downloadBtn");
const resetBtn = document.getElementById("resetBtn");

const jobDescription = document.getElementById("jobDescription");

// Candidate Info

const candidateName = document.getElementById("candidateName");
const candidateEmail = document.getElementById("candidateEmail");
const candidatePhone = document.getElementById("candidatePhone");

const atsScore = document.getElementById("atsScore");
const resumeMatch = document.getElementById("resumeMatch");

const matchedSkills = document.getElementById("matchedSkills");
const missingSkills = document.getElementById("missingSkills");

const recommendationTitle = document.getElementById("recommendationTitle");
const recommendationText = document.getElementById("recommendationText");

let lastReportUrl = "";

// ==========================
// Upload Resume
// ==========================

uploadInput.addEventListener("change", () => {

    if (!uploadInput.files.length) return;

    const file = uploadInput.files[0];

    resumeName.textContent = file.name;
    resumeSize.textContent = (file.size / 1024).toFixed(2) + " KB";

});

// ==========================
// Analyze Resume
// ==========================

analyzeBtn.addEventListener("click", async () => {

    if (!uploadInput.files.length) {
        alert("Please upload a resume.");
        return;
    }

    if (jobDescription.value.trim() === "") {
        alert("Please paste Job Description.");
        return;
    }

    analyzeBtn.disabled = true;
    analyzeBtn.innerHTML =
        '<i class="fa-solid fa-spinner fa-spin"></i> Analyzing...';

    const formData = new FormData();

    formData.append("resume", uploadInput.files[0]);
    formData.append("job_description", jobDescription.value);

    try {

        const response = await fetch("http://127.0.0.1:5000/analyze", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        if (!response.ok) {
            alert(data.error || "Server Error");
            return;
        }

        updateDashboard(data);

    } catch (error) {

        console.error(error);
        alert("Backend is not connected.");

    } finally {

        analyzeBtn.disabled = false;
        analyzeBtn.innerHTML =
            '<i class="fa-solid fa-magnifying-glass"></i> Analyze Resume';

    }

});

// ==========================
// Dashboard
// ==========================

function updateDashboard(data) {

    candidateName.textContent = data.name || "Candidate";

    candidateEmail.innerHTML =
        `<i class="fa-regular fa-envelope"></i> ${data.email || "-"}`;

    candidatePhone.innerHTML =
        `<i class="fa-solid fa-phone"></i> ${data.phone || "-"}`;

    atsScore.textContent = `${data.ats_score}%`;

    resumeMatch.textContent = `${data.resume_match}%`;

    recommendationTitle.textContent =
        data.recommendation || "Recommendation";

    recommendationText.textContent =
        data.message || "";

    lastReportUrl = data.report_url || "";

    // Matched Skills

    matchedSkills.innerHTML = "";

    if (data.matched_skills && data.matched_skills.length > 0) {

        data.matched_skills.forEach(skill => {

            matchedSkills.innerHTML += `<span>${skill}</span>`;

        });

    } else {

        matchedSkills.innerHTML = "<p>No matched skills found.</p>";

    }

    // Missing Skills

    missingSkills.innerHTML = "";

    if (data.missing_skills && data.missing_skills.length > 0) {

        data.missing_skills.forEach(skill => {

            missingSkills.innerHTML += `<span>${skill}</span>`;

        });

    } else {

        missingSkills.innerHTML = "<p>No missing skills.</p>";

    }

    // Status

    atsStatus.textContent =
        data.ats_score >= 70 ? "Good Match" :
        data.ats_score >= 40 ? "Fair Match" :
        "Low Match";

    matchStatus.textContent =
        data.resume_match >= 70 ? "Good Match" :
        data.resume_match >= 40 ? "Fair Match" :
        "Low Match";

    // Skill Overview

    skillOverview.innerHTML = "";

    const allSkills = [
        ...(data.matched_skills || []),
        ...(data.missing_skills || [])
    ];

    allSkills.forEach(skill => {

        const matched = data.matched_skills.includes(skill);

        skillOverview.innerHTML += `
            <div class="skill">
                <label>${skill}</label>

                <div class="progress">
                    <div style="width:${matched ? 100 : 0}%"></div>
                </div>

                <span>${matched ? 100 : 0}%</span>
            </div>
        `;

    });

}

// ==========================
// Download Report
// ==========================

downloadBtn.addEventListener("click", () => {

    if (!lastReportUrl) {

        alert("Please analyze a resume first.");
        return;

    }

    window.open(
        "http://127.0.0.1:5000" + lastReportUrl,
        "_blank"
    );

});

// ==========================
// Reset
// ==========================

resetBtn.addEventListener("click", () => {

    location.reload();

});