# summarizer.py
import textwrap

# OpenAI summarizer
def summarize_openai(text: str, api_key: str, max_words: int = 150, bullets: int = 5) -> str:
    import openai
    openai.api_key = api_key

    system = "You are an expert resume writer. Produce a concise set of numbered bullet points highlighting the candidate's top skills, achievements, roles, and measurable impact. Keep it professional."
    prompt = f"""Summarize the resume below into {bullets} concise bullet points (each 10-30 words), focusing on skills, roles, quantifiable achievements and relevant technologies. Use plain language and include metrics if available. Do not invent facts.

Resume:
\"\"\"{text}\"\"\"
"""

    messages = [
        {"role":"system","content":system},
        {"role":"user","content":prompt}
    ]

    # Use ChatCompletion (gpt-3.5-turbo as default)
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=0.2,
        max_tokens= max(50 + int(max_words * 2.5), 300)
    )
    out = completion.choices[0].message.content.strip()
    # Normalize into lines
    lines = [l.strip("-• \t") for l in out.splitlines() if l.strip()]
    return "\n".join(lines[:bullets])


# Local fallback using transformers pipeline (optional)
def summarize_local(text: str, max_words: int = 150, bullets: int = 5) -> str:
    # Lightweight heuristic if transformers not installed
    try:
        from transformers import pipeline
    except Exception as e:
        # Simple heuristic fallback: split into lines and pick lines with keywords
        keywords = ["experience", "worked", "led", "developed", "achieved", "improved", "reduced", "%", "increased", "decreased", "responsible"]
        lines = text.replace("\r","\n").splitlines()
        candidates = [l.strip() for l in lines if any(k in l.lower() for k in keywords)]
        bullets_out = candidates[:bullets]
        if not bullets_out:
            # fallback to first sentences
            bullets_out = [s.strip() for s in text.split(".") if s.strip()][:bullets]
        return "\n".join(bullets_out)
    # If pipeline available, use summarization
    pipe = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
    # chunk text to 1000 tokens roughly
    chunks = []
    chunk_size = 1000
    words = text.split()
    for i in range(0, len(words), chunk_size):
        chunks.append(" ".join(words[i:i+chunk_size]))

    summaries = []
    for c in chunks:
        s = pipe(c, max_length= max_words // len(chunks), min_length=30, do_sample=False)
        summaries.append(s[0]['summary_text'])
    big = " ".join(summaries)
    # Convert to bullets by splitting on sentences
    sentences = [s.strip() for s in big.replace("\n", " ").split(".") if s.strip()]
    return "\n".join(sentences[:bullets])
