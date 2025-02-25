from flask import Flask, request, jsonify

app = Flask(__name__)

# Together AI API Key (Replace with your key)
API_KEY = "cdb4c13f2cdcb4a33b24939aa7915bf9d17d0bddd5c88033dd7766e08853e698"
TOGETHER_API_URL = "https://api.together.xyz/v1/chat/completions"

@app.route("/", methods=["GET"])
def home():
    return "VoxTitan Flask API is running!", 200

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    # Dummy response (Replace with actual AI logic)
    response_text = f"AI Response to: {user_message}"

    return jsonify({"choices": [{"message": {"content": response_text}}]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
