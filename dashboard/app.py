from flask import Flask, jsonify, render_template

app = Flask(_name_)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/assistant", methods=["GET"])
def assistant():
    steps = [
        {"step": 1, "title": "Fill in personal details", "details": "Enter your name, date of birth, and contact information."},
        {"step": 2, "title": "Upload mark sheet", "details": "Attach your latest academic mark sheet in PDF format."},
        {"step": 3, "title": "Upload income certificate", "details": "Provide a valid income certificate issued by the government."},
        {"step": 4, "title": "Review eligibility", "details": "The system checks if you meet scholarship requirements."},
        {"step": 5, "title": "Submit application", "details": "Click submit to finalize your scholarship application."}
    ]
    return jsonify(steps)

if _name_ == "_main_":
    app.run(debug=True)