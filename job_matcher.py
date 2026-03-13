from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_match(resume_text, job_descriptions):

    documents = [resume_text] + job_descriptions

    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(documents)

    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:])

    results = []

    for score in similarity[0]:

        percentage = round(score * 100, 2)

        if percentage > 70:
            level = "High Match"

        elif percentage > 40:
            level = "Medium Match"

        else:
            level = "Low Match"

        results.append({
            "score": percentage,
            "level": level
        })

    return results