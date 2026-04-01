# Base Python Pura, Leve e Segura
FROM python:3.11-slim

# Previne o python de gerar arquivos inúteis de lixo na nuvem (.pyc) e força logs imediatos no Render
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Configura o diretório interno do servidor do Render
WORKDIR /app

# Copia e instala as bibliotecas.
# A cópia prévia otimiza o cache do Docker (evita demorar o build em todo deploy novo)
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia TODO o resto dos arquivos do seu projeto do Windows para o Linux do Render
COPY . /app/

# A porta Padrão para expor a API
EXPOSE 8000

# Executa o FastAPI diretamente atrelando a porta correta injetada pela variável (usada no Render)
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}"]
