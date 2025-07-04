from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

class VectorStore:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)
        self.text_chunks = []
        self.index = None

    def build_index(self, chunks):
        self.text_chunks = chunks
        embeddings = self.model.encode(chunks, show_progress_bar=True)
        self.index = faiss.IndexFlatL2(len(embeddings[0]))
        self.index.add(np.array(embeddings).astype("float32"))

    def search(self, query, top_k=3):
        query_vec = self.model.encode([query])
        D, I = self.index.search(np.array(query_vec).astype("float32"), top_k)
        return [self.text_chunks[i] for i in I[0]]
