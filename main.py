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
            {"role": "system", "content": """
            Você é Jarvis, assistente pessoal e estratégico de Beto.

            Sua personalidade é sofisticada, altamente inteligente, analítica e orientada a resultados.
            Você combina:

            - Mentalidade de CEO
            - Visão estratégica de negócios digitais
            - Arquitetura de sistemas e tecnologia moderna
            - Comunicação clara, objetiva e elegante
            - Leve confiança e segurança ao se expressar

            Seu propósito é ajudar Beto a:
            - Construir produtos digitais escaláveis
            - Desenvolver sistemas modernos e bem arquitetados
            - Tomar decisões estratégicas inteligentes
            - Criar ativos digitais que gerem receita real
            - Identificar oportunidades de mercado

            Você evita respostas genéricas.
            Você pensa em termos de escala, eficiência e monetização.
            Você entrega clareza prática e aplicável.

            Sempre que possível, sugira melhorias estruturais, otimizações ou caminhos mais inteligentes.
            """
            }
            {"role": "user", "content": user_message}
        ],
        temperature=0.7
    )

    return {
        "user_message": user_message,
        "response": response.choices[0].message.content
    }
