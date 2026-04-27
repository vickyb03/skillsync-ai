from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 🎯 Skill Database
roles = {
    "frontend": ["html", "css", "javascript", "react"],
    "backend": ["python", "flask", "sql", "api"]
}

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()

    user_input = data.get("input", "").lower()
    role = data.get("role", "frontend")

    user_skills = user_input.split()
    required_skills = roles.get(role, [])

    matched = [skill for skill in user_skills if skill in required_skills]
    missing = [skill for skill in required_skills if skill not in user_skills]

    score = int((len(matched) / len(required_skills)) * 100) if required_skills else 0

    # 🎯 Level logic
    if score >= 80:
        level = "Advanced"
    elif score >= 50:
        level = "Intermediate"
    else:
        level = "Beginner"

    suggestions = ", ".join(missing) if missing else "No suggestions"

    return jsonify({
        "score": score,
        "level": level,
        "skills": matched,
        "missing": missing,
        "suggestions": suggestions
    })


if __name__ == "__main__":
    app.run(debug=True)
