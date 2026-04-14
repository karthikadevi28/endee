from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

jobs = {
    "Data Scientist": "python machine learning data analysis",
    "Web Developer": "html css javascript",
    "Software Engineer": "java c++ algorithms",
    "Data Analyst": "excel sql python",
}

user_input = input("Enter your skills: ")

documents = list(jobs.values()) + [user_input]

vectorizer = CountVectorizer()
vectors = vectorizer.fit_transform(documents)

similarity = cosine_similarity(vectors[-1], vectors[:-1])

best_match_index = similarity.argmax()
job_list = list(jobs.keys())

print("Suggested Role:", job_list[best_match_index])
