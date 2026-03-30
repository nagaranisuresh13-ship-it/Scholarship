from flask import Flask, request, jsonify, send_file
from gtts import gTTS
import os

app = Flask(__name__)
accounts = {}

@app.route("/create", methods=["POST"])
def create_account():
    data = request.json
    accounts[data["username"]] = data["pin"]
    return jsonify({"message": "Account created!"})

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    user = data["username"]
    pin = data["pin"]
    lang = data.get("lang", "en")

    if accounts.get(user) == pin:
        messages = {
            "en": "Login successful. Welcome!",
            "hi": "लॉगिन सफल हुआ। स्वागत है!",
            "ta": "உள்நுழைவு வெற்றிகரமாக. வரவேற்கிறோம்!",
            "te": "లాగిన్ విజయవంతం. స్వాగతం!",
            "kn": "ಲಾಗಿನ್ ಯಶಸ್ವಿಯಾಗಿದೆ. ಸುಸ್ವಾಗತ!",
            "ml": "ലോഗിൻ വിജയകരം. സ്വാഗതം!",
            "mr": "लॉगिन यशस्वी. स्वागत आहे!",
            "gu": "લોગિન સફળ. સ્વાગત છે!",
            "pa": "ਲਾਗਇਨ ਸਫਲ। ਸੁਆਗਤ ਹੈ!",
            "bn": "লগইন সফল। স্বাগতম!",
            "ur": "لاگ ان کامیاب۔ خوش آمدید!",
            "or": "ଲଗଇନ ସଫଳ। ସ୍ୱାଗତ!",
            "as": "লগইন সফল। স্বাগতম!",
            "ne": "लगइन सफल। स्वागत छ!"
        }
        text = messages.get(lang, messages["en"])

        filename = f"login_{lang}.mp3"
        tts = gTTS(text=text, lang=lang)
        tts.save(filename)

        return send_file(filename, mimetype="audio/mpeg")
    else:
        return jsonify({"success": False, "message": "Invalid login"})

if __name__ == "_main_":
    app.run(debug=True)