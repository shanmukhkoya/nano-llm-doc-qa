import streamlit as st
from app.query_engine import answer_question

st.set_page_config(page_title="Nano LLM Doc QA", layout="centered")

st.title("📄 Nano LLM Document Q&A")
st.markdown("Ask a question based on the ingested documents.")

query = st.text_input("Enter your question:")

if query:
    with st.spinner("Thinking..."):
        response = answer_question(query)
        st.markdown("### 🧠 Answer:")
        st.success(response)
