import streamlit as st
import google.generativeai as genai

# --- Configuração da Página ---
st.set_page_config(
    page_title="Nexus | Influencer Factory",
    page_icon="🦾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Estilização CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@300;400;600&display=swap');
    :root {
        --primary-color: #00f2ff;
        --secondary-color: #7000ff;
        --bg-dark: #0a0b10;
    }
    .main { background-color: #0a0b10; color: #ffffff; font-family: 'Inter', sans-serif; }
    h1, h2, h3 {
        font-family: 'Orbitron', sans-serif;
        background: linear-gradient(90deg, #00f2ff, #7000ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .stButton>button {
        background: linear-gradient(45deg, #7000ff, #00f2ff);
        color: white; border-radius: 10px; font-family: 'Orbitron', sans-serif;
    }
</style>
""", unsafe_allow_html=True)

# --- Lógica de Chave de API ---
# Tenta pegar dos segredos, se não existir, fica vazio
secret_key = ""
try:
    secret_key = st.secrets["GOOGLE_API_KEY"]
except:
    secret_key = ""

api_key = st.sidebar.text_input("🔑 Gemini API Key", 
                                 value=secret_key,
                                 type="password",
                                 help="Insira sua chave do Google AI Studio.")

if not api_key:
    st.sidebar.warning("⚠️ Insira a chave de API para começar.")
    st.title("🏭 Nexus Influencer Factory")
    st.info("Bem-vindo! Insira sua API Key na barra lateral para ativar a fábrica.")
    st.stop()

genai.configure(api_key=api_key)

# --- UI Cabeçalho ---
st.title("🏭 NEXUS INFLUENCER FACTORY")
st.markdown("### Otimizador de Prompts para Produção Visual")

# --- Painel de Controle ---
with st.container():
    st.header("🪪 1. Identidade e Genética")
    col1, col2, col3 = st.columns(3)
    with col1:
        trigger_word = st.text_input("Trigger Word (LoRA)", value="Larah_Nexus")
        gender = st.selectbox("Gênero", ["Mulher", "Homem", "Não-binário"])
        age = st.slider("Idade Realista", 18, 65, 25)
    with col2:
        ethnicity = st.text_input("Etnia / Pele", value="Caucasiana, pele clara")
        body_type = st.selectbox("Estrutura Física", ["Atlética", "Magra", "Curvilínea", "Musculosa", "Natural"])
    with col3:
        hair_style = st.text_input("Cabelo", value="Loiro, longo e ondulado")
        eye_color = st.text_input("Olhares", value="Azuis")

with st.container():
    st.header("🎬 2. Ambientação e Estética")
    col4, col5 = st.columns(2)
    with col4:
        outfit = st.text_area("Look / Vestimenta", value="Look casual chic", height=100)
        location = st.text_input("Localização", value="Apartamento de luxo")
    with col5:
        action = st.text_area("Ação e Expressão", value="Sorrindo naturalmente", height=100)
        sub_col1, sub_col2 = st.columns(2)
        with sub_col1:
            lighting = st.selectbox("Iluminação", ["Luz Natural", "Cinematográfica", "Estúdio", "Neon"])
        with sub_col2:
            shot_type = st.selectbox("Enquadramento", ["Close-up", "Medium Shot", "Full Body"])

# --- Botão de Ação ---
if st.button("⚡ GENERATE PROFESSIONAL PROMPT"):
    with st.spinner("🔮 Consultando o Nexus Brain..."):
        try:
            system_prompt = f"""
            Create a detailed photorealistic AI image prompt in ENGLISH.
            Subject: {gender}, {age}yo, {ethnicity}, {body_type}. Hair: {hair_style}. Eyes: {eye_color}.
            Wearing: {outfit}. Action: {action}. Location: {location}. Lighting: {lighting}. Shot: {shot_type}.
            Rules: Start with '{trigger_word}'. Append: 'highly detailed skin texture, visible pores, raw photo, shot on 35mm, f/1.8, cinematic lighting, 8k'.
            Only the prompt, no chatter.
            """
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(system_prompt)
            st.markdown("### 🏆 Prompt Gerado")
            st.code(response.text.strip(), language="markdown")
            st.success("✨ Pronto para usar!")
        except Exception as e:
            st.error(f"⚠️ Erro: {e}")

st.markdown("---")
st.caption("Nexus Influencer Factory v1.0")
