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

const company = document.getElementById("company");
const jobRole = document.getElementById("jobRole");

// ROLES SELECTION FOR DIFFERENT COMPANIES

const roleDisplayNames = {
    "software_engineer": "Software Engineer",
    "data_analyst": "Data Analyst",
    "data_scientist": "Data Scientist",
    "machine_learning_engineer": "Machine Learning Engineer",
    "hr_manager": "HR Manager",
    "cloud_engineer": "Cloud Engineer"
};

company.addEventListener("change", async () => {
    jobRole.innerHTML = '<option value="">Select Job Role</option>';

    if (!company.value) return;

    const response = await fetch(`http://127.0.0.1:5000/roles/${company.value}`);
    const roles = await response.json();

    roles.forEach(role => {
        const option = document.createElement("option");
        option.value = roleDisplayNames[role] || role;
        option.textContent = roleDisplayNames[role] || role;
        jobRole.appendChild(option);
    });
});

// ==========================
// Candidate Info
// ==========================


const candidateName = document.getElementById("candidateName");
const candidateEmail = document.getElementById("candidateEmail");
const candidatePhone = document.getElementById("candidatePhone");

const atsScore = document.getElementById("atsScore");
const resumeMatch = document.getElementById("resumeMatch");

const matchedSkills = document.getElementById("matchedSkills");
const missingSkills = document.getElementById("missingSkills");

const recommendationTitle = document.getElementById("recommendationTitle");
const recommendationText = document.getElementById("recommendationText");


// ==========================
// Upload Resume
// ==========================

uploadInput.addEventListener("change", () => {

    if (!uploadInput.files.length) return;

    const file = uploadInput.files[0];

    resumeName.textContent = file.name;

    resumeSize.textContent =
        (file.size / 1024).toFixed(2) + " KB";

});


// ==========================
// Analyze Resume
// ==========================

analyzeBtn.addEventListener("click", async () => {

    if (!uploadInput.files.length) {

        alert("Please upload a resume first.");

        return;
    }

    if (company.value === "") {

        alert("Please select company.");

        return;
    }

    if (jobRole.value === "") {

        alert("Please select job role.");

        return;
    }

    analyzeBtn.disabled = true;

    analyzeBtn.innerHTML =
        '<i class="fa-solid fa-spinner fa-spin"></i> Analyzing...';

    const formData = new FormData();

    formData.append("resume", uploadInput.files[0]);

    formData.append("company", company.value);

    formData.append("job_role", jobRole.value);

    try {

       const response = await fetch("http://127.0.0.1:5000/analyze", {

            method: "POST",

            body: formData

        });

        if (!response.ok)
            throw new Error("Server Error");

        const data = await response.json();

        updateDashboard(data);

    }

    catch (error) {

        console.error(error);

        alert("Backend is not connected.");

    }

    finally {

        analyzeBtn.disabled = false;

        analyzeBtn.innerHTML =
            '<i class="fa-solid fa-magnifying-glass"></i> Analyze Resume';

    }

});


// ==========================
// Update Dashboard
// ==========================

function updateDashboard(data) {

    candidateName.textContent =
        data.name || "Candidate";

    lastReportUrl = data.report_url || "";
    candidateEmail.innerHTML =
        `<i class="fa-regular fa-envelope"></i> ${data.email || "-"}`;

    candidatePhone.innerHTML =
        `<i class="fa-solid fa-phone"></i> ${data.phone || "-"}`;

    atsScore.textContent =
        `${data.ats_score}%`;

    resumeMatch.textContent =
        `${data.resume_match}%`;

    recommendationTitle.textContent =
        data.recommendation || "Recommendation";

    recommendationText.textContent =
        data.message || "";

    matchedSkills.innerHTML = "";

    if (data.matched_skills) {

        data.matched_skills.forEach(skill => {

            matchedSkills.innerHTML +=

                `<span>${skill}</span>`;

        });
    

    }

    missingSkills.innerHTML = "";

    if (data.missing_skills) {

        data.missing_skills.forEach(skill => {

            missingSkills.innerHTML +=

                `<span>${skill}</span>`;

        });

    }
    atsStatus.textContent = data.ats_score >= 70 ? "Good Match" : data.ats_score >= 40 ? "Fair Match" : "Low Match";
    matchStatus.textContent = data.resume_match >= 70 ? "Good Match" : data.resume_match >= 40 ? "Fair Match" : "Low Match";

    skillOverview.innerHTML = "";
    const allRequired = [...(data.matched_skills || []), ...(data.missing_skills || [])];
    allRequired.forEach(skill => {
        const isMatched = data.matched_skills.includes(skill);
        const percent = isMatched ? 100 : 0;
        skillOverview.innerHTML += `
            <div class="skill">
                <label>${skill}</label>
                <div class="progress"><div style="width:${percent}%"></div></div>
                <span>${percent}%</span>
            </div>
        `;
    });
}


// ==========================
// Download Report
// ==========================

let lastReportUrl = "";

downloadBtn.addEventListener("click", () => {
    if (lastReportUrl) {
        window.open("http://127.0.0.1:5000" + lastReportUrl);
    } else {
        alert("Please analyze a resume first.");
    }
});


// ==========================
// Reset
// ==========================

resetBtn.addEventListener("click", () => {

    location.reload();

});