# Install required libraries
!pip install deep-translator transformers sentencepiece

# Imports
from deep_translator import GoogleTranslator
from transformers import pipeline

# Supported languages (Google Translator codes)
LANGUAGES = {
    'Afrikaans': 'af', 'Arabic': 'ar', 'Bengali': 'bn', 'Chinese (Simplified)': 'zh-cn',
    'French': 'fr', 'German': 'de', 'Gujarati': 'gu', 'Hindi': 'hi',
    'Japanese': 'ja', 'Korean': 'ko', 'Punjabi': 'pa', 'Russian': 'ru',
    'Spanish': 'es', 'Tamil': 'ta', 'Telugu': 'te'
}

# Hugging Face MarianMT models map (common pairs)
HF_MODELS = {
    ("en", "fr"): "Helsinki-NLP/opus-mt-en-fr",
    ("fr", "en"): "Helsinki-NLP/opus-mt-fr-en",
    ("en", "de"): "Helsinki-NLP/opus-mt-en-de",
    ("de", "en"): "Helsinki-NLP/opus-mt-de-en",
    ("en", "es"): "Helsinki-NLP/opus-mt-en-es",
    ("es", "en"): "Helsinki-NLP/opus-mt-es-en",
    ("en", "hi"): "Helsinki-NLP/opus-mt-en-hi",
    ("hi", "en"): "Helsinki-NLP/opus-mt-hi-en",
}

# ----------------------------
# User input
# ----------------------------
text = input("✍ Enter text to translate: ")

print("\nAvailable languages:", ", ".join(LANGUAGES.keys()))
source_lang = input("Select source language (or type 'auto' for auto-detect): ")
target_lang = input("Select target language: ")

method = input("Choose translation method - type 'google' or 'huggingface': ").strip().lower()

# ----------------------------
# Translation
# ----------------------------
try:
    if method == "google":
        # Google Translator
        translated_text = GoogleTranslator(
            source="auto" if source_lang.lower() == "auto" else LANGUAGES.get(source_lang, "auto"),
            target=LANGUAGES.get(target_lang, "en")
        ).translate(text)

    elif method == "huggingface":
        # Hugging Face MarianMT
        src_code = "auto" if source_lang.lower() == "auto" else LANGUAGES.get(source_lang, "en")
        tgt_code = LANGUAGES.get(target_lang, "fr")  # default to French if not found

        if (src_code, tgt_code) not in HF_MODELS:
            raise ValueError(f"No Hugging Face model available for {src_code} → {tgt_code}")

        model_name = HF_MODELS[(src_code, tgt_code)]
        translator = pipeline("translation", model=model_name)
        translated_text = translator(text)[0]['translation_text']

    else:
        raise ValueError("Invalid method. Please choose 'google' or 'huggingface'.")

    print("\n✅ Translation Successful!")
    print("📝 Translated Text:", translated_text)

except Exception as e:
    print(f"\n❌ Translation failed: {e}")
