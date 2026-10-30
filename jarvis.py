import ollama
arquivo = open("sobre-mim.md", encoding="utf-8")
texto = arquivo.read()
pergunta = input("Você: ")
resposta = ollama.generate(model="qwen2.5:7b", system=texto, prompt=pergunta)
print("Jarvis:", resposta["response"])
