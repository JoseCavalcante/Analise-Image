# 🚀 Plataforma de Análise de Imagens com IA

Uma poderosa API desenvolvida em Python e alimentada pelo **FastAPI**, **Agno** e **Google Gemini (Generative AI)**, projetada para a automação e análise avançada de imagens enviadas por usuários.

O projeto conta com uma estrutura robusta em Backend que interage dinamicamente com as imagens, garantindo limpeza em disco e segurança.

## ✨ Funcionalidades

- **Endpoint FastAPI (`/api/upload`)**: Rotas isoladas para recebimento ágil de uploads do tipo `multipart/form-data`.
- **Validação de Formatos**: Proteções de backend contra arquivos indesejados (somente imagens jpeg/png, etc).
- **Processamento com IA**: O Agno, integrado com a tecnologia Gemini LLM da Google, avalia a imagem e responde estruturadamente com base no `prompt` via Markdown.
- **Eficiência de Armazenamento**: Imagens são salvas temporariamente na pasta `/upload_img_enviadas` sendo automaticamente deletadas após a avaliação da IA ser finalizada.
- **Preparado para Nuvem**: `Dockerfile` pronto e otimizado com permissões de execução (Unix-LF) para implantação direta e automática de containers em serviços como Render ou AWS.
- **Integração CORS Flexível**: Preparado para suportar futuras UIs ou Módulos Front-End modernos consumindo o back-end via porta única (`$PORT`).

---

## 🛠 Pré-requisitos e Instalação

Antes de começar, é preciso rodar os passos no terminal de preferência para configurar as bibliotecas vitais:

1. Clone o projeto e acesse o diretório principal.
2. Crie e ative um ambiente virtual (recomendado):
   ```bash
   python -m venv venv
   .\venv\Scripts\activate      # No Windows
   source venv/bin/activate     # No Linux/Mac
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Crie o seu arquivo vital `.env` na raiz do projeto contendo a Chave Secreta da API do Google, que vai energizar o seu Agno/Gemini:
   ```env
   GOOGLE_API_KEY=sua-chave-aqui
   ```

---

## 💻 Como Rodar (Localmente)

Com as váriaveis e dependências estipuladas, a mágica acontece executando apenas um comando nativo do FastAPI (Uvicorn):

```bash
uvicorn main:app --reload
```
A API ficará acessível no seu navegador via: `http://localhost:8000`

Para testar ou debugar os endpoints com uma roleta de interações Swagger UI, acesse:
👉 `http://localhost:8000/docs`

> *Nota:* A versão legada baseada no visual em Streamlit pode ser chamada no terminal lateral via `streamlit run streamlit_app.py`.

---

## ☁️ Deploy (Produção em Nuvem)

A aplicação foi rigorosamente testada com a nuvem moderna visando escalabilidade em contêiners (`Docker`).

Caso suba para plataformas Serverless e CaaS Web Services (**Render**, **Railway**), o Container buscará na nuvem a Variável de Ambiente: `$PORT`, atribuída dinamicamente. Para funcionar, basta:

1. Integrar este Repositório ao Render
2. Selecionar o plano `Docker`
3. Informar o Segredo `GOOGLE_API_KEY` na aba de Ambiente Avançado (Settings > Environment)
4. Fazer Deploy! O próprio Render converterá e provisionará nosso `Dockerfile`.

## 💼 Tecnologias

- Python 3.11+
- FastAPI & Uvicorn
- Google Generative AI (Gemini)
- Docker
- Agno
