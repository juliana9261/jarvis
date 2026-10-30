#!/bin/bash
# Guarda a chave do Groq que está no copiar-colar no .env, sem mostrá-la.
cd "$(dirname "$0")"
chave=$(pbpaste | tr -d '[:space:]')
if [[ "$chave" != gsk_* ]]; then
  echo "❌ O que está copiado não é uma chave do Groq (deveria começar com gsk_). Copie a chave no site e rode de novo."
  exit 1
fi
echo "GROQ_API_KEY=$chave" > .env
status=$(curl -s -o /dev/null -w '%{http_code}' https://api.groq.com/openai/v1/models -H "Authorization: Bearer $chave")
[ "$status" = "200" ] && echo "✅ Chave guardada e aceita pelo Groq." || echo "⚠️ Chave guardada, mas o Groq respondeu $status."
