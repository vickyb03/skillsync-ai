from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "SkillSync AI Backend Running 🚀"

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    text = data.get("input", "").lower()
    link = data.get("link", "").lower()
    role = data.get("role", "backend")

    # Role-based skills
    roles = {
        "backend": ["python", "flask", "api", "sql"],
        "frontend": ["html", "css", "javascript", "react"],
        "data": ["python", "sql", "excel", "powerbi"]
    }

    job_skills = roles.get(role, [])

    # Simulated link extraction
    if "coursera" in link:
        text += " python sql machine learning"
    elif "linkedin" in link:
        text += " python flask api communication"

    # Matching
    matched = [s for s in job_skills if s in text]
    missing = list(set(job_skills) - set(matched))

    # Weighted scoring
    weights = {s: 2 for s in job_skills}
    total_weight = sum(weights.values())
    matched_weight = sum(weights[s] for s in matched)

    score = int((matched_weight / total_weight) * 100) if total_weight else 0

    # Skill level
    if score >= 80:
        level = "Advanced"
    elif score >= 50:
        level = "Intermediate"
    else:
        level = "Beginner"

    # Suggestions
    suggestions = [f"Learn {s}" for s in missing]

    return jsonify({
        "score": score,
        "skills": matched,
        "missing": missing,
        "level": level,
        "suggestions": suggestions
    })

if __name__ == '__main__':
    app.run(debug=True)
