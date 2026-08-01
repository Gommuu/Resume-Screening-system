from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(resume_text, job_description_text):
    documents = [resume_text, job_description_text]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)
    similarity_score = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])
    return similarity_score[0][0]


from resume_parser import extract_text_from_pdf
from preprocessing import clean_text

if __name__ == "__main__":
    raw_text = extract_text_from_pdf("../dataset/R4.pdf")
    cleaned_resume = clean_text(raw_text)

    job_description = "Looking for a software engineer skilled in Python, JavaScript, MySQL, and Node.js."
    cleaned_job = clean_text(job_description)

    score = calculate_similarity(cleaned_resume, cleaned_job)
    print("Similarity Score:", score)