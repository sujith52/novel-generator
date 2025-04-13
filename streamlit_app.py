import streamlit as st
import google.generativeai as genai

# 🔑 Replace with your actual Gemini API key
genai.configure(api_key="AIzaSyBD8FxH90_NPS1PvgCPpJYZExwJYCWoSUQ")

# Prompt templates for genres
PROMPT_TEMPLATES = {
    "fantasy": "Write a fantasy novel chapter involving dragons, magic, and a mysterious kingdom.",
    "system": "Write a system-based novel chapter where the protagonist levels up using a game-like interface.",
    "sci-fi": "Write a sci-fi novel chapter with futuristic technology and space exploration.",
    "romance": "Write a romantic novel chapter between two characters from different worlds.",
    "adventure": "Write an adventurous chapter where the hero faces unexpected challenges in a jungle."
}

def generate_chapter(tag: str, word_count: int) -> str:
    if tag not in PROMPT_TEMPLATES:
        raise ValueError(f"Unsupported tag '{tag}'. Available tags: {list(PROMPT_TEMPLATES.keys())}")

    prompt = PROMPT_TEMPLATES[tag] + f" The chapter should be around {word_count} words long."

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)

    return response.text

# Streamlit UI
st.title("📖 AI Novel Chapter Generator")

selected_tag = st.selectbox(
    "Choose a genre:",
    list(PROMPT_TEMPLATES.keys())
)

word_count = st.slider("Select desired word count:", min_value=100, max_value=3000, step=100, value=500)

if st.button("Generate Chapter"):
    with st.spinner("Generating... please wait"):
        try:
            chapter = generate_chapter(selected_tag, word_count)
            st.subheader("Generated Chapter")
            st.write(chapter)
        except Exception as e:
            st.error(f"Error: {e}")
