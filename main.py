from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://keerthi-kumar-k-j.github.io/Vox-Titan/"],  # Change this to specific origins in production
    allow_credentials=True,
    allow_methods=["POST","GET"],
    allow_headers=["*"],
)

# Replace with your actual free AI API endpoint & key
AI_API_URL = "https://api.together.ai/v1/chat/completions"  
API_KEY = "cdb4c13f2cdcb4a33b24939aa7915bf9d17d0bddd5c88033dd7766e08853e698"

# Request model
class UserInput(BaseModel):
    message: str

@app.post("/chat")
async def chat(user_input: UserInput):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo",  # Change to a supported free model if needed
        "messages": [{"role": "user", "content": user_input.message}]
    }

    response = requests.post(AI_API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        ai_response = response.json()
        return {"response": ai_response["choices"][0]["message"]["content"]}
    else:
        raise HTTPException(status_code=500, detail="AI response failed")

@app.get("/")
async def root():
    return {"message": "VoxTitan API is running!"}
