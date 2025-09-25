import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(
    page_title="Multilingual Translator",
    page_icon="🌐",
    layout="centered"
)

LANGUAGES = {
    'Afrikaans': 'af', 'Arabic': 'ar', 'Bengali': 'bn', 'Chinese (Simplified)': 'zh-CN',
    'French': 'fr', 'German': 'de', 'Gujarati': 'gu', 'Hindi': 'hi', 'Japanese': 'ja',
    'Korean': 'ko', 'Punjabi': 'pa', 'Russian': 'ru', 'Spanish': 'es',
    'Tamil': 'ta', 'Telugu': 'te'
}

st.markdown(
    """
    <style>
    .title {text-align: center; font-size: 40px; font-weight: bold; color: #4CAF50;}
    .footer {text-align: center; font-size: 14px; margin-top: 30px; color: gray;}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 class='title'>🌐 Multilingual Translator</h1>", unsafe_allow_html=True)

text = st.text_area("✍ Enter text to translate:", height=150, placeholder="Type or paste your text here...")

col1, col2 = st.columns(2)
with col1:
    source_lang = st.selectbox("Select source language", ["Auto-detect"] + sorted(LANGUAGES.keys()))
with col2:
    target_lang = st.selectbox("Select target language", sorted(LANGUAGES.keys()))

if st.button("🔄 Translate"):
    if not text.strip():
        st.warning("⚠️ Please enter some text to translate.")
    else:
        try:
            src = "auto" if source_lang == "Auto-detect" else LANGUAGES[source_lang]
            tgt = LANGUAGES[target_lang]
            translated_text = GoogleTranslator(
                source=src,
                target=tgt
            ).translate(text)
            st.success("✅ Translation Successful!")
            st.text_area("🐍 Translated Text:", translated_text, height=150)
        except Exception as e:
            st.error(f"❌ Translation failed: {e}")

st.markdown("<p class='footer'>Made with ❤ using Streamlit & Google Translator API</p>", unsafe_allow_html=True)