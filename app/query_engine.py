from sentence_transformers import SentenceTransformer
import chromadb
from app.llm_runner import call_openrouter_llm

def answer_question(question):
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_collection("docs")

    model = SentenceTransformer("all-MiniLM-L6-v2")
    question_embedding = model.encode(question).tolist()

    results = collection.query(query_embeddings=[question_embedding], n_results=4)
    retrieved_docs = results['documents'][0]

    context = "\n\n".join(retrieved_docs)

    prompt = f"""Use the following document context to answer the question.

    Context:
    {context}

    Question: {question}
    """

    return call_openrouter_llm(prompt)
