from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

TOGETHER_API_KEY = "cdb4c13f2cdcb4a33b24939aa7915bf9d17d0bddd5c88033dd7766e08853e698"

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = requests.post(
        "https://api.together.xyz/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {TOGETHER_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo",  # Or any other model
            "messages": [{"role": "user", "content": user_input}]
        }
    )
    return jsonify({"response": response.json()['choices'][0]['message']['content']})

if __name__ == '__main__':
    app.run(debug=True)
