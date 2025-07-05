import glob
import chromadb
from sentence_transformers import SentenceTransformer
import fitz  # PyMuPDF
import docx

def extract_text(file_path):
    if file_path.endswith(".pdf"):
        text = ""
        with fitz.open(file_path) as doc:
            for page in doc:
                text += page.get_text()
        return text

    elif file_path.endswith(".docx"):
        doc = docx.Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])

    elif file_path.endswith(".txt") or file_path.endswith(".md"):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()

    return ""

def chunk_text(text, chunk_size=300, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

def ingest_docs():
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_or_create_collection("docs")

    embedder = SentenceTransformer("all-MiniLM-L6-v2")

    supported_exts = (".pdf", ".docx", ".txt", ".md")
    files = [f for f in glob.glob("data/*") if f.lower().endswith(supported_exts)]

    doc_id = 0

    for file in files:
        print(f"Ingesting: {file}")
        text = extract_text(file)
        chunks = chunk_text(text)

        # Filter out empty chunks
        filtered_chunks = [chunk for chunk in chunks if chunk.strip() != ""]

        if not filtered_chunks:
            print(f"Skipping {file} as it has no valid text chunks.")
            continue

        embeddings = embedder.encode(filtered_chunks).tolist()
        ids = [f"doc_{doc_id}_{i}" for i in range(len(filtered_chunks))]
        doc_id += 1

        collection.add(
            documents=filtered_chunks,
            embeddings=embeddings,
            ids=ids
        )

    print("✅ Ingestion complete!")

if __name__ == "__main__":
    ingest_docs()
