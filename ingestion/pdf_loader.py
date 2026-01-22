import pdfplumber

def load_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for p in pdf.pages:
            text += (p.extract_text() or "") + "\n"
    return text