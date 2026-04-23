"""
College Enquiry Chatbot - Flask Web Application
"""

import os
from flask import Flask, render_template, request, jsonify, session
from chatbot import CollegeChatbot

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "college-chatbot-secret-2024")

# Initialize chatbot (loaded once at startup)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
chatbot = CollegeChatbot(intents_path=os.path.join(BASE_DIR, "Dataset", "intents.json"))


@app.route("/")
def home():
    """Serve the college website home page."""
    return render_template("home.html")


@app.route("/chat")
def chat_page():
    """Serve the chatbot UI (embedded in iframe)."""
    session.setdefault("history", [])
    return render_template("index.html")


@app.route("/api/chat", methods=["POST"])
def api_chat():
    """
    POST /chat
    Body: { "message": "user text" }
    Returns: { "response": "...", "tag": "...", "confidence": 0.0 }
    """
    data = request.get_json(silent=True)
    if not data or "message" not in data:
        return jsonify({"error": "No message provided"}), 400

    user_message = str(data["message"]).strip()
    result = chatbot.get_response(user_message)

    # Store in session history (last 20 exchanges)
    history = session.get("history", [])
    history.append({"user": user_message, "bot": result["response"]})
    session["history"] = history[-20:]

    return jsonify(result)


@app.route("/history", methods=["GET"])
def history():
    """Return current session chat history."""
    return jsonify({"history": session.get("history", [])})


@app.route("/clear", methods=["POST"])
def clear():
    """Clear session chat history."""
    session["history"] = []
    return jsonify({"status": "cleared"})


@app.route("/health", methods=["GET"])
def health():
    """Health check endpoint."""
    return jsonify({"status": "ok", "intents_loaded": len(chatbot.intents)})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
