from fastapi import FastAPI
import requests

app = FastAPI()

API_KEY = "cdb4c13f2cdcb4a33b24939aa7915bf9d17d0bddd5c88033dd7766e08853e698"  # Replace with your actual API key

@app.get("/")
def home():
    return {"message": "VoxTitan API is running!"}

@app.post("/chat")
def chat(user_input: str):
    url = "https://api.together.ai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "meta-llama/Llama-3.3-70B-Instruct-Turbot",  # Update to your working model
        "messages": [{"role": "user", "content": user_input}]
    }
    
    response = requests.post(url, headers=headers, json=data)
    return response.json()

