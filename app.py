# app.py
import streamlit as st
from summarizer import summarize_openai, summarize_local
from parser_utils import extract_text_from_file
import os

st.set_page_config(page_title="Resume Summarizer (GenAI)", layout="centered")
st.title("✅ Resume Summarizer (GenAI)")

st.sidebar.header("Settings")
mode = st.sidebar.selectbox("Summarization mode", ["OpenAI (recommended)", "Local Transformer (fallback)"])
openai_key = st.sidebar.text_input("OpenAI API Key (if using OpenAI)", type="password")
max_length = st.sidebar.slider("Max summary length (words)", 50, 600, 150)
num_points = st.sidebar.slider("Number of bullet points", 3, 12, 5)

uploaded_file = st.file_uploader("Upload resume (PDF, TXT, DOCX not supported here)", type=['pdf','txt'])
or_example = st.checkbox("Use example resume (sample_resumes/sample_resume.txt)")

if or_example:
    path = os.path.join("sample_resumes","sample_resume.txt")
    with open(path, 'r', encoding='utf-8') as f:
        resume_text = f.read()
else:
    resume_text = ""
    if uploaded_file is not None:
        resume_text = extract_text_from_file(uploaded_file)

if not resume_text:
    st.info("Upload a resume (PDF or TXT) or tick 'Use example resume' to try.")
    st.stop()

st.header("Resume (extracted)")
with st.expander("Show extracted resume text"):
    st.write(resume_text[:10000])  # show a slice if very long

st.write("---")
if st.button("Generate Summary"):
    with st.spinner("Generating summary..."):
        if mode.startswith("OpenAI"):
            if not openai_key:
                st.error("OpenAI API key required for OpenAI mode. Enter it in sidebar.")
                st.stop()
            summary = summarize_openai(
                text=resume_text,
                api_key=openai_key,
                max_words=max_length,
                bullets=num_points
            )
        else:
            # local
            summary = summarize_local(
                text=resume_text,
                max_words=max_length,
                bullets=num_points
            )

    st.success("Summary generated")
    st.subheader("Summary — Bullet Points")
    for i, b in enumerate(summary.split("\n")):
        if b.strip():
            st.markdown(f"{i+1}. {b.strip()}")
    st.download_button("Download summary (txt)", summary, file_name="resume_summary.txt")
