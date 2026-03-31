from flask import Flask, jsonify, render_template
import datetime

app = Flask(_name_)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/blockchain", methods=["GET"])
def blockchain():
    # Demo blockchain-style log
    blocks = [
        {"block": 1, "timestamp": str(datetime.datetime.now()), "scholarship": "National Merit", "status": "Submitted", "hash": "abc123"},
        {"block": 2, "timestamp": str(datetime.datetime.now()), "scholarship": "National Merit", "status": "Under Review", "hash": "def456"},
        {"block": 3, "timestamp": str(datetime.datetime.now()), "scholarship": "National Merit", "status": "Approved", "hash": "ghi789"}
    ]
    return jsonify(blocks)

if _name_ == "_main_":
    app.run(debug=True)