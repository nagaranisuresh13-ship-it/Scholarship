from flask import Flask, request, jsonify, render_template

app = Flask(_name_)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.json
    marks = data.get("marks")
    income = data.get("income")

    # Simple hackathon-style logic
    if marks >= 85 and income == "low":
        result = [{"name": "National Merit Scholarship", "amount": 5000, "probability": 95}]
    elif marks >= 70:
        result = [{"name": "Tech Excellence Award", "amount": 3000, "probability": 80}]
    else:
        result = [{"name": "Community Support Grant", "amount": 2000, "probability": 60}]

    return jsonify(result)

if _name_ == "_main_":
    app.run(debug=True)