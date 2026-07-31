from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from preprocessing import preprocess_text


def calculate_similarity(resume_text, job_description):
    """
    Calculates similarity score between resume and job description.
    Returns score in percentage.
    """

    # Clean both texts
    resume_text = preprocess_text(resume_text)
    job_description = preprocess_text(job_description)

    # Convert text into TF-IDF vectors
    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform([resume_text, job_description])

    # Calculate cosine similarity
    score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]

    # Convert into percentage
    return round(score * 100, 2)


# ----------------------------
# Test
# ----------------------------

if __name__ == "__main__":

    resume = """
    Python SQL Machine Learning Flask Git Pandas NumPy
    """

    job_description = """
    Looking for a Python Developer with SQL, Flask and Git experience.
    """

    similarity = calculate_similarity(resume, job_description)

    print(f"Similarity Score : {similarity}%")