python
import streamlit as st
import google.generativeai as genai

# --- Configuração da Página ---
st.set_page_config(
    page_title="Nexus | Influencer Factory",
    page_icon="🦾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Estilização CSS Superior (Premium / Cyberpunk / Glassmorphism) ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@300;400;600&display=swap');

    :root {
        --primary-color: #00f2ff;
        --secondary-color: #7000ff;
        --bg-dark: #0a0b10;
        --glass-bg: rgba(255, 255, 255, 0.05);
        --glass-border: rgba(255, 255, 255, 0.1);
    }

    .main {
        background-color: var(--bg-dark);
        color: #ffffff;
        font-family: 'Inter', sans-serif;
    }

    h1, h2, h3 {
        font-family: 'Orbitron', sans-serif;
        background: linear-gradient(90deg, #00f2ff, #7000ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        letter-spacing: 2px;
    }

    /* Glassmorphism Containers */
    div.stBlock {
        background: var(--glass-bg);
        border: 1px solid var(--glass-border);
        border-radius: 15px;
        padding: 20px;
        backdrop-filter: blur(10px);
        margin-bottom: 20px;
    }

    /* Customizing Buttons */
    .stButton>button {
        background: linear-gradient(45deg, #7000ff, #00f2ff);
        color: white;
        border: none;
        padding: 15px 30px;
        border-radius: 10px;
        font-family: 'Orbitron', sans-serif;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 2px;
        transition: all 0.3s ease;
        box-shadow: 0 0 15px rgba(0, 242, 255, 0.3);
    }

    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 0 25px rgba(112, 0, 255, 0.6);
        color: white;
    }

    /* Sidebar Styling */
    .css-1d391kg {
        background-color: #0d0e14;
    }

    /* Inputs Styling */
    .stTextInput>div>div>input {
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid var(--glass-border);
        color: white;
    }

    /* Footer / Caption */
    .footer {
        text-align: center;
        padding: 20px;
        font-size: 0.8em;
        color: #666;
    }
</style>
""", unsafe_allow_html=True)

# --- Lógica de Chave de API ---
# Prioridade: 1. st.secrets (para online) | 2. Input Manual (para desenvolvimento)
api_key = st.sidebar.text_input("🔑 Gemini API Key", 
                                 value=st.secrets.get("GOOGLE_API_KEY", ""),
                                 type="password",
                                 help="Obtenha sua chave no Google AI Studio. Se configurado nos segredos do Streamlit, aparecerá aqui automaticamente.")

if not api_key:
    st.sidebar.warning("⚠️ Chave de API ausente. Insira para ativar a IA.")
    st.title("🏭 Nexus Influencer Factory")
    st.info("Bem-vindo à Fábrica de Influenciadores. Por favor, insira sua Gemini API Key na barra lateral para começar a criar.")
    st.stop()

genai.configure(api_key=api_key)

# --- UI Cabeçalho ---
st.title("🏭 NEXUS INFLUENCER FACTORY")
st.markdown("### Otimizador de Prompts para Produção Visual de Alta Performance")

# --- Painel de Controle Principal ---
with st.container():
    st.header("🪪 1. Identidade e Genética")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        trigger_word = st.text_input("Trigger Word (LoRA)", value="Larah_Nexus", help="Nome do modelo treinado.")
        gender = st.selectbox("Gênero", ["Mulher", "Homem", "Não-binário"])
        age = st.slider("Idade Realista", 18, 65, 25)
    
    with col2:
        ethnicity = st.text_input("Etnia / Detalhes de Pele", value="Caucasiana, pele oliva", placeholder="Ex: Brasileira parda, Asiática Coreana")
        body_type = st.selectbox("Estrutura Física", ["Atlética/Definida", "Magra/Elegante", "Curvilínea/Fit", "Musculosa", "Média/Natural"])
    
    with col3:
        hair_style = st.text_input("Cabelo", value="Morena, fios longos e brilhantes")
        eye_color = st.text_input("Olhares", value="Castanhos amendoados")

st.markdown("---")

with st.container():
    st.header("🎬 2. Ambientação e Estética")
    col4, col5 = st.columns(2)
    
    with col4:
        outfit = st.text_area("Look / Vestimenta", value="Look casual chic, regata branca de seda e jeans premium", height=100)
        location = st.text_input("Localização / Background", value="Apartamento de luxo em SP, vista através da janela, final de tarde")
    
    with col5:
        action = st.text_area("Ação e Expressão", value="Olhando para a câmera com um sorriso leve e natural, segurando uma xícara de café", height=100)
        
        sub_col1, sub_col2 = st.columns(2)
        with sub_col1:
            lighting = st.selectbox("Iluminação", ["Luz Natural / Golden Hour", "Iluminação Cinematográfica", "Soft Studio Light", "Neon / Cyberpunk", "Hard Shadow / High Contrast"])
        with sub_col2:
            shot_type = st.selectbox("Enquadramento", ["Close-up (Rosto)", "Medium Shot (Cintura)", "Full Body (Corpo)", "Pov Shot"])

# --- Configurações Avançadas de IA ---
with st.sidebar:
    st.divider()
    st.subheader("⚙️ Configurações de IA")
    realism_mode = st.toggle("Ultra-Realismo Ativado", value=True)
    target_model = st.selectbox("Motor de Imagem", ["FLUX.1 [Dev]", "Krea AI", "Midjourney v6.1"])
    creativity = st.slider("Nível de Detalhamento da IA", 0.1, 1.0, 0.7)

# --- Botão de Ação ---
if st.button("⚡ GENERATE PROFESSIONAL PROMPT"):
    with st.spinner("🔮 Consultando o Nexus Brain..."):
        try:
            # Engenharia de Prompt para o Gemini
            system_prompt = f"""
            Role: Expert Image Prompt Engineer for {target_model}.
            Objective: Create a high-end, detailed, and photorealistic AI image prompt in ENGLISH.
            
            Subject: {gender}, {age} years old, {ethnicity}, {body_type} body.
            Features: {hair_style}, {eye_color}.
            Wearing: {outfit}.
            Action: {action}.
            Location: {location}.
            Lighting & Shot: {lighting}, {shot_type}.
            
            Technical Rules:
            1. Language: English.
            2. Start with '{trigger_word}' (essential).
            3. Use natural language, descriptive adjectives, and focus on textures.
            4. Realism Booster ({realism_mode}): If True, append 'highly detailed skin texture, visible pores, hyper-realistic, raw photo, shot on 35mm lens, f/1.8, cinematic lighting, 8k resolution, authentic textures'.
            5. No chatter. Only the prompt.
            """
            
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(system_prompt)
            prompt_final = response.text.strip()
            
            # Resultado Glassmorphism
            st.markdown("### 🏆 Prompt Gerado")
            st.code(prompt_final, language="markdown")
            
            st.success("✨ Prompt pronto para ser usado no Krea.ai ou Flux!")
            
            st.info("💡 **Dica da Fábrica:** Se estiver usando no Krea, mantenha o 'Strength' do LoRA em 0.9 para máxima fidelidade à Larah.")

        except Exception as e:
            st.error(f"⚠️ Erro ao acessar o cérebro da IA: {e}")

st.markdown("<div class='footer'>Nexus Influencer Factory v1.0 | Made for High Performance Teams</div>", unsafe_allow_html=True)
