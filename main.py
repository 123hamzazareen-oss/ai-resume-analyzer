from flask import Flask, render_template, request, redirect
from database import create_tables
from auth import register_user, login_user
from resume_parser import parse_resume
from skill_extractor import extract_skills
from resume_score import calculate_score
from resume_suggestion import generate_suggestions
from job_matcher import calculate_match
from job_description import jobs as job_db

app = Flask(__name__)

create_tables()


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/register", methods=["GET","POST"])
def register():

    if request.method == "POST":

        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        register_user(username, email, password)

        return redirect("/")

    return render_template("register.html")


@app.route("/login", methods=["POST"])
def login():

    email = request.form["email"]
    password = request.form["password"]

    user = login_user(email, password)

    if user:
        return redirect("/upload")

    return "Invalid Login"


@app.route("/upload", methods=["GET","POST"])
def upload():

    if request.method == "POST":

        file = request.files["resume"]

        text = parse_resume(file)

        skills = extract_skills(text)

        score, missing = calculate_score(skills)

        suggestions = generate_suggestions(missing)

        # resume text for matching
        resume_text = " ".join(skills)

        job_titles = list(job_db.keys())
        job_descriptions = []

        for j in job_db.values():
            job_descriptions.append(" ".join(j))

        matches = calculate_match(resume_text, job_descriptions)

        jobs = []

        for i, m in enumerate(matches):

            jobs.append({
                "job_id": job_titles[i],
                "level": m["level"],
                "score": m["score"]
            })

        # ⭐ SORT BY SCORE
        jobs = sorted(jobs, key=lambda x: x["score"], reverse=True)

        # ⭐ TOP 5 JOBS
        jobs = jobs[:5]

        return render_template(
            "dashboard.html",
            score=score,
            skills=skills,
            missing=missing,
            suggestions=suggestions,
            jobs=jobs
        )

    return render_template("upload.html")


if __name__ == "__main__":
    app.run(debug=True)