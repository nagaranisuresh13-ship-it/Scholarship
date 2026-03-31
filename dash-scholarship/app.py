from flask import Flask, jsonify, render_template

app = Flask(_name_)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard", methods=["GET"])
def dashboard():
    applications = [
        {"name": "National Merit Scholarship", "status": "Submitted", "deadline": "2026-04-15"},
        {"name": "Tech Excellence Award", "status": "Under Review", "deadline": "2026-05-01"},
        {"name": "Community Support Grant", "status": "Approved", "deadline": "2026-03-30"},
        {"name": "Sports Talent Grant", "status": "Missing Documents", "deadline": "2026-04-10"}
    ]
    return jsonify(applications)

if _name_ == "_main_":
    app.run(debug=True)