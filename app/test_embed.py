from ingest import load_documents
from clean_chunk import clean_text, chunk_text
from embed_store import VectorStore

# Step 1: Load and prepare document chunks
docs = load_documents("../data")
chunks = []

for _, content in docs:
    cleaned = clean_text(content)
    chunks += chunk_text(cleaned, max_words=150)

# Step 2: Create vector store
store = VectorStore()
store.build_index(chunks)

# Step 3: Ask a question
query = "What is CCaaS?"
results = store.search(query, top_k=3)

# Step 4: Show results
print("\nTop Results:")
for r in results:
    print("------")
    print(r[:500])
