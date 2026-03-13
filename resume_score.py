required_skills = [
"python","machine learning","data analysis","sql","tensorflow","pandas",
"numpy","scikit-learn","flask","django","docker","git",
"html","css","javascript","react","aws","linux",
"power bi","tableau","nlp","deep learning"
]

def calculate_score(resume_skills):

    matched = []
    missing = []

    for skill in required_skills:

        if skill in resume_skills:
            matched.append(skill)

        else:
            missing.append(skill)

    score = (len(matched)/len(required_skills))*100

    return round(score,2),missing