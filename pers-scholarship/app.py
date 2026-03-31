from flask import Flask, request, jsonify, render_template

app = Flask(_name_)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/personalized", methods=["POST"])
def personalized():
    data = request.json
    marks = data.get("marks")
    category = data.get("category")
    interests = data.get("interests")

    results = []

    # Simple hackathon-style personalization logic
    if marks >= 85:
        results.append({"name": "Merit Excellence Scholarship", "reason": "High academic performance"})
    if category == "SC/ST":
        results.append({"name": "Social Equity Scholarship", "reason": "Reserved category support"})
    if "sports" in interests.lower():
        results.append({"name": "Sports Talent Grant", "reason": "Recognized for sports achievements"})
    if "tech" in interests.lower():
        results.append({"name": "Tech Innovators Award", "reason": "Interest in technology and innovation"})

    if not results:
        results.append({"name": "General Support Scholarship", "reason": "Basic eligibility"})

    return jsonify(results)

if _name_ == "_main_":
    app.run(debug=True)