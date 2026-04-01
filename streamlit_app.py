import streamlit as st
import requests

# Endereço base da sua API construída anteriormente
API_URL = "http://localhost:8000/api/upload"

# Configuração da Página
st.set_page_config(
    page_title="Análise de Imagens com IA",
    page_icon="🌌",
    layout="centered"
)

# Header
st.title("🌌 Análise de Imagens com IA")
st.markdown("Faça upload de uma imagem e veja nosso **Agente Gemini** em ação através do modelo *Flash 2.5*.")

st.divider()

# Container de Upload
upload_file = st.file_uploader(
    
    "Arraste a sua imagem aqui (JPEG, PNG, WEBP)", 
    type=["jpg", "jpeg", "png", "webp"]
)

if upload_file is not None:
    # Exibir a imagem enviada (preview local)
    st.image(upload_file, caption="Pré-visualização da imagem", use_container_width=True)
    
    # Campo de Instrução para a IA
    custom_prompt = st.text_area(
        "Instruções para a Inteligência Artificial:",
        value="Descreva detalhadamente o que você vê nesta imagem, listando elementos importantes."
    )
    
    # Botão de Ação
    if st.button("✨ Analisar com IA", use_container_width=True):
        
        # Estado de Carregamento
        with st.spinner('A visão robótica está processando a imagem...'):
            try:
                # Payload contendo a Imagem e o Texto
                files = {"file": (upload_file.name, upload_file.getvalue(), upload_file.type)}
                data = {"prompt": custom_prompt}
                
                # Executar POST Request na porta padrão do uvicorn
                response = requests.post(API_URL, files=files, data=data)
                
                # Sucesso HTTP
                if response.status_code == 200:
                    data = response.json()
                    st.success("Análise concluída com sucesso!")
                    
                    st.divider()
                    st.subheader("📋 Relatório do Agente:")
                    # O streamlit converte o markdown automaticamente com este widget
                    st.markdown(data.get("analise", "Resposta não encontrada."))
                    
                # Erro de Backend/API
                else:
                    try:
                        err_msg = response.json().get("detail", "Erro desconhecido")
                    except:
                        err_msg = response.text
                    st.error(f"O servidor recusou a análise. Detalhes: {err_msg}")
                    
            except requests.exceptions.ConnectionError:
                st.error("🚨 Erro Crítico: O Servidor FastAPI não está online! Por favor, abra um terminal e inicie o servidor rodando 'uvicorn main:app'.")
            
            except Exception as e:
                st.error(f"🚨 Ocorreu um erro no processo: {str(e)}")

# --- Rodapé da Página (Footer) ---
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown(
    """
    <div style="text-align: center; color: #94a3b8; font-size: 0.9em; padding-top: 10px; border-top: 1px solid rgba(255,255,255,0.1);">
        Criado e desenvolvido por <b>Jacn Soluções em IA</b><br>
        Contato: +55 21 99188-7787
    </div>
    """,
    unsafe_allow_html=True
)
