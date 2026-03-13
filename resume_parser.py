import pdfplumber
import docx

def parse_resume(file):

    text = ""

    if file.filename.endswith(".pdf"):

        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text

    elif file.filename.endswith(".docx"):

        doc = docx.Document(file)
        for para in doc.paragraphs:
            text += para.text

    return text