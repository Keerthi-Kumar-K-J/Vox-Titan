from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Together AI API Key (Replace with your key)
API_KEY = "cdb4c13f2cdcb4a33b24939aa7915bf9d17d0bddd5c88033dd7766e08853e698"
TOGETHER_API_URL = "https://api.together.xyz/v1/chat/completions"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message")

    if not user_message:
        return jsonify({"error": "Message is required"}), 400

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo",  # Change model if needed
        "messages": [{"role": "user", "content": user_message}],
        "max_tokens": 100
    }

    response = requests.post(TOGETHER_API_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to fetch AI response"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
