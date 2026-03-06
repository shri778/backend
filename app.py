from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Shrinivas Electricals Assistant Running"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "").lower()

    # Greeting
    if "hi" in message or "hello" in message:
        reply = "Hello! Welcome to Shrinivas Electricals. How can I help you?"

    # Bulb colours
    elif "bulb" in message and ("colour" in message or "color" in message):
        reply = "We have multi colour bulbs and warm white bulbs."

    # Bulb companies
    elif "company" in message or "companies" in message:
        reply = "We have Revor, Jaguar, Oplus and Bajaj companies."

    # Bulb watt
    elif "watt" in message or "volt" in message:
        reply = "We have 5W, 7W, 10W and 15W bulbs."

    # Batteries
    elif "battery" in message:
        reply = "We have high quality batteries available in our shop."

    # Unknown question
    else:
        reply = "I can't help you with that. Please ask about bulbs, batteries or companies."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)