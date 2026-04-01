#!/bin/bash

# Este script fará o papel de "Maestro" do container.
# Ele iniciará o Backend e o Frontend dentro da mesma máquina para não gastarmos
# múltiplos Web Services no pacote gratuito da plataforma.

# 1. Inicia o Backend FastAPI rodando "em background" (Sinal & no final).
# O Render não exibe a porta 8000 da máquina para fora, então ela ficará segura
# apenas rodando internamente no servidor.
echo "Iniciando a API Interna (Uvicorn) na porta 8000..."
uvicorn main:app --host 0.0.0.0 --port 8000 &

# 2. Aguarda 3 segundos pro FastAPI 'respirar' e inicializar forte antes da UI
sleep 3

# 3. Inicia o Streamlit (Frontend) na Porta que o Render determinar 
# (Através da Variável de ambiente $PORT que o provedor injeta pra nós no Container)
echo "Iniciando a Interface de Usuário (Streamlit) na porta externa $PORT..."
streamlit run streamlit_app.py --server.port ${PORT:-8501} --server.address 0.0.0.0 
