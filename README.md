# Jarvis

[![Converse com o meu Jarvis](https://img.shields.io/badge/🤖_Converse_com_o_meu_Jarvis-e0b44c?style=for-the-badge)](https://jarvis-juliana.onrender.com)

Assistente pessoal com IA que responde perguntas sobre mim, meus estudos e meus projetos, com humor no estilo do J.A.R.V.I.S. do Homem de Ferro e resposta em voz.

No ar, roda no [Render](https://render.com) com a IA do [Groq](https://groq.com) (modelo `openai/gpt-oss-120b`). No computador, sem chave do Groq, usa um modelo local (Qwen 2.5 7B, via [Ollama](https://ollama.com)). A voz é a do navegador de quem acessa. Tudo nos planos gratuitos.

## Como funciona

```
Navegador (index.html) ──POST /perguntar──▶ servidor.py (FastAPI) ──▶ Groq na nuvem, ou Ollama no computador
        ▲                                         │  usa sobre-mim.md como instrução
        └──────────── resposta em JSON ◀──────────┘
        e fala a resposta com a voz do navegador
```

| Arquivo | O que faz |
|---|---|
| `sobre-mim.md` | O conhecimento e a personalidade do Jarvis. Ele só sabe o que está escrito aqui |
| `jarvis.py` | Versão de terminal: conversa até digitar `sair`, e fala as respostas |
| `servidor.py` | A API: `POST /perguntar` recebe a pergunta e devolve a resposta; `GET /` entrega a página |
| `index.html` | A página de chat |
| `teste_ia.py` | O primeiro teste de conversa com a IA |

## Como rodar

Precisa do [Ollama](https://ollama.com) instalado e do modelo baixado:

```bash
ollama pull qwen2.5:7b
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

Versão web:

```bash
.venv/bin/uvicorn servidor:app
```

Depois abra http://localhost:8000. A documentação da API fica em http://localhost:8000/docs.

Versão de terminal (com voz, no macOS):

```bash
.venv/bin/python jarvis.py
```

## Decisões

- **Temperatura 0.2:** com a temperatura padrão, o modelo inventava fatos (chegou a inventar meu signo e dizer que estava nos arquivos). Baixa, ele se prende ao que está escrito.
- **Few-shot:** em vez de só descrever o tom, o `sobre-mim.md` traz exemplos de respostas. O modelo imita exemplos melhor do que segue descrições.
- **Regras no topo do arquivo:** modelos menores dão mais peso ao que vem primeiro.

## Próximos passos

- Voz mais natural.
