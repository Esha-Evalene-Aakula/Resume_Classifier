import streamlit as st
from transformers import pipeline
import docx2txt

st.title("Resume Summarizer")

# Upload resume
uploaded_file = st.file_uploader("Upload your resume (PDF/DOCX)", type=["pdf", "docx"])

if uploaded_file:
    # Convert DOCX to text
    if uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        text = docx2txt.process(uploaded_file)
    else:
        text = uploaded_file.read().decode("utf-8")

    # Load summarization pipeline
    summarizer = pipeline("summarization")

    # Generate summary
    summary = summarizer(text, max_length=200, min_length=50, do_sample=False)
    st.subheader("Resume Summary")
    st.write(summary[0]['summary_text'])
