def recommend_jobs(skills):

    jobs = []

    if "python" in skills:
        jobs.append("Python Developer")

    if "machine learning" in skills:
        jobs.append("ML Engineer")

    if "data analysis" in skills:
        jobs.append("Data Analyst")

    if "django" in skills:
        jobs.append("Backend Developer")

    return jobs