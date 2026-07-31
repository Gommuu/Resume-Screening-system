// ===========================
// Resume Preview
// ===========================

const previewBtn = document.querySelector(".preview-btn");

if (previewBtn) {

    previewBtn.addEventListener("click", () => {

        alert("Resume Preview will be available after backend integration.");

    });

}

// ===========================
// Analyze Resume
// ===========================

const analyzeBtn = document.querySelector(".analyze-btn");

if (analyzeBtn) {

    analyzeBtn.addEventListener("click", () => {

        alert("Backend not connected yet.");

    });

}

// ===========================
// Download Report
// ===========================

const downloadBtn = document.querySelector(".download-btn");

if (downloadBtn) {

    downloadBtn.addEventListener("click", () => {

        alert("Report generation will be available after backend integration.");

    });

}

// ===========================
// Analyze Another Resume
// ===========================

const anotherBtn = document.querySelector(".another-btn");

if (anotherBtn) {

    anotherBtn.addEventListener("click", () => {

        location.reload();

    });

}

// ===========================
// Back to Home
// ===========================

const homeBtn = document.querySelector(".home-btn");

if (homeBtn) {

    homeBtn.addEventListener("click", () => {

        window.scrollTo({

            top:0,

            behavior:"smooth"

        });

    });

}