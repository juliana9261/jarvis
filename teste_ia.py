import ollama
resposta = ollama.generate(model="qwen2.5:7b", prompt="Diga olá em uma frase")
print(resposta["response"])
