import ollama
from fastapi import FastAPI
from fastapi.responses import FileResponse
import os
import httpx
from dotenv import load_dotenv
load_dotenv()
chave = os.getenv("GROQ_API_KEY")
app = FastAPI()
arquivo = open("sobre-mim.md", encoding="utf-8")
texto = arquivo.read()
@app.post("/perguntar")
def perguntar(dados: dict):
    if chave:
        r = httpx.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={"Authorization": "Bearer " + chave},
            json={
                "model": "openai/gpt-oss-120b",
                "temperature": 0.2,
                "messages": [
                    {"role": "system", "content": texto},
                    {"role": "user", "content": dados["pergunta"]},
                ],
            },
            timeout=60,
        )
        resposta = r.json()["choices"][0]["message"]["content"]
    else:
        resposta = ollama.generate(model="qwen2.5:7b", system=texto, prompt=dados["pergunta"], options={"temperature": 0.2})["response"]
    return {"resposta": resposta}
@app.get("/")
def pagina():
    return FileResponse("index.html")
