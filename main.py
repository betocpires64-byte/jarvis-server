from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ChatRequest(BaseModel):
    message: str

@app.api_route("/",methods=["GET","HEAD"])
def root():
    return {"status": "Jarvis Server Online 🚀"}

@app.post("/chat")
def chat(request: ChatRequest):
    user_message = request.message
    
    # resposta simples por enquanto
    return {
        "user_message": user_message,
        "response": f"Você disse: {user_message}"
    }

