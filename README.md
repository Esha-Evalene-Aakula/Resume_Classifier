##**Resume Summarizer & Classifier**

**Overview**

The Resume Summarizer & Classifier is a web-based application that automatically extracts and summarizes key information from resumes. It helps recruiters and hiring managers quickly evaluate candidate profiles without manually reviewing full documents.The system supports resumes in PDF and DOCX formats and uses a pretrained natural language processing model to generate concise summaries.

**Objective**

- Automatically summarize resumes into key highlights
- Reduce manual resume screening time
- Provide a structured and concise overview of candidate profiles

**Tech Stack**

- Programming Language -> Python 3.10+
- NLP Model	-> Hugging Face Transformers (Pretrained Summarization Model)
- Deep Learning Backend	-> PyTorch
- Data Handling (Optional)	-> Pandas
- Web Framework	-> Streamlit / Gradio / Flask
- Resume Parsing	-> docx2txt, PyPDF2

**Key Features**

- Upload resumes in PDF or DOCX format
- Automatic text extraction
- AI-powered resume summarization
- Web-based interface for ease of use
- Fast and scalable inference

**Implementation Workflow**

1. Upload a resume (PDF or DOCX) through the web interface
2. Extract text from the uploaded file
    - DOCX processed using docx2txt
    - PDF processed using PyPDF2
3. Preprocess extracted text to remove noise and formatting issues
4. Generate a summary using a pretrained Hugging Face summarization pipeline
5. Display the summarized content on the web application


**Project Structure**

resume-classifier/
│── app.py              # Streamlit web application
│── parser_utils.py     # Utilities for parsing PDF and DOCX resumes
│── summarizer.py       # NLP summarization logic using Hugging Face
│── requirements.txt    # Project dependencies
│── README.md           # Project documentation


**Future Enhancements**

- Resume classification by job role or domain
- Skill extraction and keyword-based scoring
- Multi-language resume support
- Export summaries as PDF or JSON
- ATS relevance and compatibility scoring

**Conclusion**

The Resume Summarizer & Classifier simplifies resume evaluation by leveraging modern NLP techniques to generate concise and meaningful summaries. It is suitable for academic projects, recruitment automation, and AI-driven hiring workflows.
