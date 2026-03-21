from flask import Flask, request, jsonify

app = Flask(__name__)

job_skills = ["python", "flask", "sql", "api"]

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    text = data.get("input", "").lower()

    user_skills = [s for s in job_skills if s in text]

    score = int((len(user_skills)/len(job_skills)) * 100)
    missing = list(set(job_skills) - set(user_skills))

    return jsonify({
        "score": score,
        "skills": user_skills,
        "missing": missing
    })