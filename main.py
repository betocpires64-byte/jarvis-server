from fastapi import FastAPI
from pydantic import BaseModel
import os
from openai import OpenAI

app = FastAPI()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class ChatRequest(BaseModel):
    message: str

@app.api_route("/", methods=["GET", "HEAD"])
def root():
    return {"status": "Jarvis AI Online 🚀"}

@app.post("/chat")
def chat(request: ChatRequest):
    user_message = request.message

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Você é Jarvis, um assistente inteligente e objetivo."},
            {"role": "user", "content": user_message}
        ],
        temperature=0.7
    )

    return {
        "user_message": user_message,
        "response": response.choices[0].message.content
    }
