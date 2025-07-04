from ingest import load_documents
from clean_chunk import clean_text, chunk_text

docs = load_documents("../data")

for name, content in docs:
    print(f"\n--- {name} ---")
    cleaned = clean_text(content)
    chunks = chunk_text(cleaned, max_words=150)
    print(f"Total chunks: {len(chunks)}")
    print(f"Sample chunk:\n{chunks[0][:500]}")
