from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)   # Allow all frontend requests (fixes your issue)

# Dummy users (for login)
users = {
    "admin": "1234",
    "vignesh": "1234"
}

# Skills required for job
job_skills = ["python", "flask", "sql", "api"]

# 🔐 LOGIN API
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if username in users and users[username] == password:
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "fail"})

# 🧠 ANALYZE API
@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    text = data.get("input", "").lower()

    user_skills = [s for s in job_skills if s in text]

    score = int((len(user_skills) / len(job_skills)) * 100)
    missing = list(set(job_skills) - set(user_skills))

    return jsonify({
        "score": score,
        "skills": user_skills,
        "missing": missing
    })

# 🏠 Optional Home Route (to avoid 404)
@app.route('/')
def home():
    return "SkillSync AI Backend Running 🚀"

# Run app (for local testing)
if __name__ == '__main__':
    app.run(debug=True)
