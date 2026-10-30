import ollama
import subprocess
arquivo = open("sobre-mim.md", encoding="utf-8")
texto = arquivo.read()
while True:
    pergunta = input("Você: ")
    if pergunta == "sair": break
    resposta = ollama.generate(model="qwen2.5:7b", system=texto, prompt=pergunta, options={"temperature": 0.2})
    print("Jarvis:", resposta["response"])
    subprocess.run(["say", "-v", "Luciana", "-r", "165", resposta["response"]])
