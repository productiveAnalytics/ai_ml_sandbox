# Streamlit app

import streamlit as st

from chatbot import *

st.title("🌐 Gemini 2.0 Flash-Lite Translator")

target_language = st.sidebar.selectbox(
    'User language',
    ('Spanish', 'French', 'German', 'Hindi', 'Arabic')
)

text_to_translate = st.text_area("Enter English text to translate")

@st.cache_resource
def initialize_app():
    configure_api_key()

    return initialize_genai() # return model and prompt template

if st.button("Translate") and text_to_translate and target_language:
    try:
        genai_model, prompt_template = initialize_app()
        response_txt = launch_chat_app(genai_model, prompt_template, user_language=target_language, user_text=text_to_translate)
        st.success(f"**Translation ({target_language}):**\n\n{response_txt.strip()}")
    except Exception as e:
        st.error(f"Translation failed: {e}")

st.caption("Powered by Steamlit and Google Gemini 2.0 Flash-Lite")