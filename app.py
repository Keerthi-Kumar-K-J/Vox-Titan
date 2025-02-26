from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

TOGETHER_API_KEY = "cdb4c13f2cdcb4a33b24939aa7915bf9d17d0bddd5c88033dd7766e08853e698"

@app.route('/chat', methods=['POST'])
def chat():
    # Get the JSON data from the request
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({"error": "Invalid request, 'message' field is required"}), 400

    user_input = data['message']

    try:
        # Call Together.ai API
        response = requests.post(
            "https://api.together.xyz/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {TOGETHER_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo",  # Replace with your model
                "messages": [{"role": "user", "content": user_input}]
            }
        )
        response.raise_for_status()  # Raise an error for bad status codes

        # Extract the AI's response
        ai_response = response.json()['choices'][0]['message']['content']
        return jsonify({"response": ai_response})

    except requests.exceptions.RequestException as e:
        # Handle API request errors
        return jsonify({"error": f"Failed to call Together.ai API: {str(e)}"}), 500
    except KeyError as e:
        # Handle missing keys in the response
        return jsonify({"error": f"Invalid response from Together.ai API: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
