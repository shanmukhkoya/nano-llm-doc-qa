## 📌 Project Overview

### 🧠 Description

**Nano LLM Document QA** is a lightweight, local-first Question Answering (QA) system built to allow users to ask questions about their documents using a small, fast, and efficient language model. It is specifically designed to work on resource-constrained systems without requiring internet access or large cloud APIs.

### 🎯 Project Goals

* Ingest and vectorize documents locally
* Store and search embeddings using FAISS
* Use a compact LLM (like GPT4All, LLaMA.cpp, or TinyLLM) to answer user queries
* Serve a simple interface for querying documents
* Minimal dependencies to ensure it's fast and lightweight

### 🚦 Project Phase: Initial Working Prototype ✅

We have successfully completed the first phase of the project:

* 🔹 Local ingestion and chunking of documents
* 🔹 Embedding with FAISS
* 🔹 Querying via RetrievalQA
* 🔹 Code pushed to GitHub

We are now transitioning into the **next development phase**, which will focus on:

* 🔸 UI for user interaction (simple web/chat interface)
* 🔸 Replacing remote models with fully local LLMs (like llama.cpp)
* 🔸 Optimization and performance tuning
* 🔸 Packaging and documentation

---

## 🛠️ Step-by-Step: How We Built This Project

### Step 1: 🏗️ Create Project Structure

We started by creating a directory:

```bash
mkdir nano-llm-doc-qa
cd nano-llm-doc-qa
```

### Step 2: 🐍 Setup Python Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
```

### Step 3: 📦 Install Required Libraries

We installed the basic dependencies:

```bash
pip install langchain faiss-cpu openai python-dotenv
```

*Depending on the LLM used, other libraries like `llama-cpp-python` or `gpt4all` may be included later.*

### Step 4: 📄 Load and Split Documents

We used LangChain’s `DirectoryLoader` and `TextSplitter` to load and chunk documents:

```python
from langchain.document_loaders import DirectoryLoader
from langchain.text_splitter import CharacterTextSplitter
```

We split long documents into smaller chunks for embedding.

### Step 5: 🧠 Generate Embeddings

We used embedding models like `OpenAIEmbeddings` or local models for creating vector representations of each chunk.

### Step 6: 📚 Store Embeddings in FAISS

FAISS is used for fast similarity search:

```python
from langchain.vectorstores import FAISS
```

We saved and reloaded the FAISS index to persist data.

### Step 7: 🤖 Answer Queries

We connected the retriever to a chain that uses a language model to answer questions based on the most relevant document chunks:

```python
from langchain.chains import RetrievalQA
```

We used either a local LLM or a cloud-hosted one for response generation.

### Step 8: 🧪 Testing the App

We tested using CLI or a minimal Python script to query the vectorstore and get accurate answers.

### Step 9: 📋 Create `.gitignore`

Avoid unnecessary files in Git:

```
venv/
__pycache__/
*.pyc
*.pkl
*.faiss
.env
```

### Step 10: 📂 Create GitHub Repo & Push Code

Followed the GitHub steps to initialize the repo, commit files, and push to GitHub (see below).

---

## ✅ GitHub Push Instructions (Recap)

### **🧩 Prerequisites**

1. Install Git:

```bash
sudo apt update
sudo apt install git
```

2. Configure Git:

```bash
git config --global user.name "Shanmukh Koya"
git config --global user.email "your_email@example.com"
```

### **🌐 Create GitHub Repository**

1. Go to GitHub → New Repository → Name: `nano-llm-doc-qa`
2. Don’t initialize with README
3. Copy the repo URL

### **📦 Go to Project Folder**

```bash
cd ~/nano-llm-doc-qa
```

### **📸 Initialize and Push**

```bash
git init
git add .
git commit -m "Initial commit - Nano LLM Doc QA project"
git remote add origin https://github.com/yourusername/nano-llm-doc-qa.git
git branch -M main
git push -u origin main
