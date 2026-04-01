import os
from agno.agent import Agent
from agno.models.google import Gemini
from agno.media import Image as AgnoImage

def analisar_imagem(caminho_imagem: str, prompt: str) -> str:
    """
    Usa um Agente Gemini Vision para descrever detalhadamente
    o conteúdo da imagem enviada pelo usuário.
    """
    try:
        agente = Agent(
            model=Gemini(id="gemini-2.5-flash"), # Usa o modelo mais rápido de visão da Google (ou 1.5/2.0 dependendo da defult API da versão instalada)
            description="Você é um assistente cirúrgico e especialista em análise de imagens com alta precisão descritiva."
        )

        imagem = AgnoImage(filepath=caminho_imagem)

        resposta = agente.run(
            prompt,
            images=[imagem]
        )

        return resposta.content
    except Exception as e:
        return f"Erro ao analisar imagem: {str(e)}"
