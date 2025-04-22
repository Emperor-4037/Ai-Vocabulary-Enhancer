import streamlit as st
import google.generativeai as genai
import os

# Configure Gemini API key securely
api_key = os.getenv("GEMINI_API_KEY") or st.secrets.get("GEMINI_API_KEY")

if not api_key:
    st.error("❌ Gemini API key not found. Set it in secrets or as an environment variable.")
    st.stop()

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-pro")

st.set_page_config(page_title="AI Vocabulary Enhancer", layout="centered")
st.title("📚 AI Vocabulary Enhancer")
st.write("Boost your vocabulary using Google's Gemini AI!")

text = st.text_input("Enter a word or sentence")
mode = st.selectbox("Select Enhancement Type", ["Synonyms", "Definition", "Sentence Rewriting", "Advanced Vocabulary Suggestions"])

if st.button("Enhance"):
    if not text.strip():
        st.warning("Please enter a word or sentence.")
    else:
        with st.spinner("Generating..."):
            prompt = ""
            if mode == "Synonyms":
                prompt = f"List advanced and varied synonyms for: {text}"
            elif mode == "Definition":
                prompt = f"Define '{text}' in simple terms and give a usage example."
            elif mode == "Sentence Rewriting":
                prompt = f"Rewrite this sentence using richer vocabulary: {text}"
            elif mode == "Advanced Vocabulary Suggestions":
                prompt = f"Suggest advanced words that can replace '{text}', with explanation."

            try:
                response = model.generate_content(prompt)
                st.success("✅ Result:")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Something went wrong: {e}")
