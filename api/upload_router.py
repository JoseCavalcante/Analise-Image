from fastapi import APIRouter, UploadFile, File, HTTPException, Form
from servicos.file_service import garantir_pasta_persistente
from servicos.analysis_service import analisar_imagem
import os

router = APIRouter()

# Usa o serviço para garantir que a pasta existe
UPLOAD_DIR = garantir_pasta_persistente("upload_img_enviadas")


@router.post("/upload")
async def upload_arquivo(
    file: UploadFile = File(...), 
    prompt: str = Form("Descreva detalhadamente o que você vê nesta imagem, listando elementos importantes.")
):
    """
    Recebe um arquivo do usuário, valida se é imagem, 
    analisa com o Gemini e exclui o arquivo para poupar disco.
    """
    
    # Validação Básica de Arquivo
    if not file.content_type.startswith('image/'):
        raise HTTPException(
            status_code=400, 
            detail="Arquivo inválido. Por favor, envie uma imagem (jpeg, png, etc)."
        )

    caminho_arquivo = UPLOAD_DIR / file.filename

    # Salva o arquivo original
    with open(caminho_arquivo, "wb") as buffer:
        conteudo = await file.read()
        buffer.write(conteudo)

    # Executa a análise baseada no Gemini
    resultado_analise = analisar_imagem(str(caminho_arquivo), prompt)

    # Limpeza: Deleta a imagem pós-análise
    if caminho_arquivo.exists():
        os.remove(caminho_arquivo)

    return {
        "mensagem": "Imagem processada com sucesso!",
        "arquivo": file.filename,
        "analise": resultado_analise
    }
