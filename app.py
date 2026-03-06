from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Shrinivas Electricals AI is running"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "").lower()

    # Greeting
    if "hi" in message or "hello" in message:
        reply = "Hello! Welcome to Shrinivas Electricals. How can I help you?"

    # Bulb colors
    elif "bulb" in message and "colour" in message or "color" in message:
        reply = "We have multi colour bulbs, warm white bulbs and other varieties."

    # Bulb companies
    elif "company" in message or "companies" in message or "brand" in message:
        reply = "We have companies like Revor, Jaguar, Oplus and Bajaj."

    # Bulb watt
    elif "watt" in message or "volt" in message:
        reply = "We have 5W, 7W, 10W and 15W bulbs."

    # Battery
    elif "battery" in message or "batteries" in message:
        reply = "We have high quality batteries available in our shop."

    # Default response
    else:
        reply = "I can't help you with that. You can ask about batteries, bulb colours or companies we have."

    return jsonify({"reply": reply})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)