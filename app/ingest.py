import os
import fitz  # PyMuPDF
import pandas as pd
from docx import Document

def read_pdf(file_path):
    doc = fitz.open(file_path)
    return "\n".join([page.get_text() for page in doc])

def read_docx(file_path):
    doc = Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

def read_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def read_csv(file_path):
    df = pd.read_csv(file_path)
    return df.to_string()

def load_documents(folder_path):
    docs = []
    for filename in os.listdir(folder_path):
        path = os.path.join(folder_path, filename)
        if filename.endswith(".pdf"):
            docs.append((filename, read_pdf(path)))
        elif filename.endswith(".docx"):
            docs.append((filename, read_docx(path)))
        elif filename.endswith(".txt"):
            docs.append((filename, read_txt(path)))
        elif filename.endswith(".csv"):
            docs.append((filename, read_csv(path)))
    return docs
