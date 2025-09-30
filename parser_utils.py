import io
import pdfplumber

def extract_text_from_file(uploaded_file):
    name = uploaded_file.name.lower()
    if name.endswith('.txt'):
        raw = uploaded_file.read().decode('utf-8', errors='ignore')
        return raw
    elif name.endswith('.pdf'):
        # read via pdfplumber
        with pdfplumber.open(io.BytesIO(uploaded_file.read())) as pdf:
            pages = [p.extract_text() or "" for p in pdf.pages]
        return "\n\n".join(pages)
    else:
        raise ValueError("Unsupported file type. Please upload PDF or TXT.")
