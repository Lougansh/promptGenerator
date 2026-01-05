# 🤖 Nexus Influencer Factory - Guia de Deploy

Este guia explica como colocar sua "Fábrica de Influenciadores" online para que sua equipe possa usar em qualquer lugar.

---

## 🚀 Passo 1: Criar um Repositório no GitHub
1. Acesse [github.com](https://github.com) e faça login (ou crie uma conta).
2. Clique no botão **"New"** (Novo) para criar um repositório.
3. Dê um nome ao projeto (ex: `nexus-factory`).
4. Deixe como **Public** (Público) ou **Private** (Privado).
5. Clique em **"Create repository"**.
6. Suba os arquivos `app.py` e `requirements.txt` que estão na pasta `c:\ProjetoRF\GeradorPromptKrea`.

## 🌐 Passo 2: Publicar no Streamlit Cloud
1. Acesse [share.streamlit.io](https://share.streamlit.io).
2. Conecte sua conta do GitHub.
3. Clique em **"New app"**.
4. Selecione o repositório `nexus-factory`.
5. No campo **"Main file path"**, verifique se está escrito `app.py`.
6. **IMPORTANTE (Segurança):** Antes de clicar em Deploy:
   - Clique em **"Advanced settings..."**.
   - No campo **"Secrets"**, cole o seguinte (substituindo pela sua chave real):
     ```toml
     GOOGLE_API_KEY = "SUA_CHAVE_AQUI"
     ```
7. Clique em **"Deploy!"**.

## ✅ Passo 3: Usar e Compartilhar
- Em 1 ou 2 minutos, o app estará online.
- O Streamlit vai te dar um link (ex: `nexus-factory.streamlit.app`).
- Compartilhe esse link com sua equipe!

---
> [!TIP]
> **Dica de Segurança:** Nunca compartilhe sua Chave API em conversas públicas. Ao usar os "Secrets" do Streamlit, sua chave fica protegida e não aparece no código.
