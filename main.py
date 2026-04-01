import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from api.upload_router import router as upload_img_enviadas_analise_router

# Carrega as variáveis do .env (ex: GOOGLE_API_KEY)
load_dotenv()

app = FastAPI(
    title="Antigravity Anal Image API",
    description="API para upload e análise de imagens enviadas",
    version="1.0.0"
)

# Configuração de CORS para permitir requisições de frontends (ex: React, Vue)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Troque para os domínios reais em produção
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclui os roteadores (endpoints)
app.include_router(upload_img_enviadas_analise_router, prefix="/api", tags=["upload"])

@app.get("/")
def home():
    return {"message": "API rodando! Acesse /docs para testar os endpoints."}