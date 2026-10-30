import ollama
from fastapi import FastAPI
from fastapi.responses import FileResponse
app = FastAPI()
arquivo = open("sobre-mim.md", encoding="utf-8")
texto = arquivo.read()
@app.post("/perguntar")
def perguntar(dados: dict):
    resposta = ollama.generate(model="qwen2.5:7b", system=texto, prompt=dados["pergunta"], options={"temperature": 0.2})
    return {"resposta": resposta["response"]}
@app.get("/")
def pagina():
    return FileResponse("index.html")
