from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)
from datetime import datetime
import os


def generate_report(
    filename,
    name,
    email,
    phone,
    company,
    job_role,
    ats_score,
    resume_match,
    matched_skills,
    missing_skills,
    recommendation,
):
    """
    Generate a professional PDF report for the analyzed resume.
    """

    os.makedirs("reports", exist_ok=True)

    filepath = os.path.join("reports", filename)

    doc = SimpleDocTemplate(filepath)

    styles = getSampleStyleSheet()

    elements = []

    # ================= Title =================

    title = Paragraph(
        "<b><font size='20'>AI Resume Screening Report</font></b>",
        styles["Title"],
    )

    elements.append(title)

    elements.append(Spacer(1, 20))

    # ================= Date =================

    generated = Paragraph(
        f"<b>Generated On:</b> {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}",
        styles["Normal"],
    )

    elements.append(generated)

    elements.append(Spacer(1, 20))

    # ================= Candidate Details =================

    data = [
        ["Candidate Name", name],
        ["Email", email],
        ["Phone", phone],
        ["Company", company],
        ["Job Role", job_role],
        ["ATS Score", f"{ats_score}%"],
        ["Resume Match", f"{resume_match}%"],
        ["Recommendation", recommendation],
    ]

    table = Table(data, colWidths=[160, 320])

    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#2563EB")),
                ("TEXTCOLOR", (0, 0), (0, -1), colors.white),
                ("BACKGROUND", (1, 0), (1, -1), colors.whitesmoke),
                ("GRID", (0, 0), (-1, -1), 1, colors.grey),
                ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 8),
            ]
        )
    )

    elements.append(table)

    elements.append(Spacer(1, 25))

    # ================= Matched Skills =================

    elements.append(
        Paragraph(
            "<b>Matched Skills</b>",
            styles["Heading2"],
        )
    )

    elements.append(
        Paragraph(
            ", ".join(matched_skills) if matched_skills else "None",
            styles["BodyText"],
        )
    )

    elements.append(Spacer(1, 20))

    # ================= Missing Skills =================

    elements.append(
        Paragraph(
            "<b>Missing Skills</b>",
            styles["Heading2"],
        )
    )

    elements.append(
        Paragraph(
            ", ".join(missing_skills) if missing_skills else "None",
            styles["BodyText"],
        )
    )

    elements.append(Spacer(1, 20))

    # ================= Summary =================

    elements.append(
        Paragraph(
            "<b>Summary</b>",
            styles["Heading2"],
        )
    )

    summary = (
        f"The candidate achieved an ATS Score of <b>{ats_score}%</b> "
        f"with a Resume Match score of <b>{resume_match}%</b>. "
        f"Recommendation: <b>{recommendation}</b>."
    )

    elements.append(
        Paragraph(
            summary,
            styles["BodyText"],
        )
    )

    doc.build(elements)

    return filepath


# ================= TEST =================

if __name__ == "__main__":

    report = generate_report(
        filename="sample_report.pdf",
        name="Vansh Gupta",
        email="vansh@example.com",
        phone="9876543210",
        company="Google",
        job_role="Software Engineer",
        ats_score=90,
        resume_match=88,
        matched_skills=[
            "python",
            "sql",
            "git",
            "docker",
        ],
        missing_skills=[
            "aws",
        ],
        recommendation="Strong Candidate - Recommended",
    )

    print("Report Generated:", report)