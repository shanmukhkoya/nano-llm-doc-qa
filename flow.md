```mermaid
graph TD
    A[Start: User uploads or places document in /data] --> B[Read & Split using LangChain]
    B --> C[Generate Embeddings using Sentence Transformers]
    C --> D[Store in ChromaDB (local vector DB)]
    D --> E[User asks question via CLI or UI]
    E --> F[Retrieve relevant chunks from ChromaDB]
    F --> G[Send context + question to OpenRouter LLM]
    G --> H[Return generated answer to user]
    H --> Z[End]
```
