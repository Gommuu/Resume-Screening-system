import os
import pdfplumber
from docx import Document


def extract_text_from_pdf(pdf_path):

    text = ""

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:

                text += page_text + "\n"

    return text


def extract_text_from_docx(docx_path):

    document = Document(docx_path)

    text = ""

    for paragraph in document.paragraphs:

        text += paragraph.text + "\n"

    return text


def extract_resume_text(file_path):

    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":

        return extract_text_from_pdf(file_path)

    elif extension == ".docx":

        return extract_text_from_docx(file_path)

    else:

        raise ValueError("Unsupported file format. Please upload PDF or DOCX.")


if __name__ == "__main__":

    sample = "../dataset/Resume.pdf"

    print(extract_resume_text(sample))