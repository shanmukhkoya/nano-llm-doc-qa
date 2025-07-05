## 📌 Project Overview

### 🧠 What Is This Project?

**Nano LLM Document QA** is a beginner-friendly, lightweight document-based Question Answering system. You upload documents (PDF or Word), and the system allows you to ask natural language questions based on the content. It's designed to:

* Run on machines with limited resources (like WSL or cloud PCs)
* Use local file storage
* Work even without internet (once everything is set up)
* Help you learn Python, LLMs (Language Models), and app development step-by-step

---

## 🎯 Project Goals

1. 🔍 **Understand your documents** using AI
2. 🧠 Use small but powerful LLMs (like Mistral, GPT4All, etc.)
3. 💾 Store document info using a fast local database (ChromaDB)
4. 🔗 Ask questions and get answers through a terminal or a web UI (Streamlit)
5. 📦 Keep the setup simple and installable with basic Python knowledge

---

## ✅ What’s Working Now (as of today)

✔️ Ingesting PDFs or Word docs
✔️ Generating vector embeddings using OpenRouter’s LLM API
✔️ Storing them locally in ChromaDB
✔️ Asking questions via a command-line test script or web UI
✔️ Running completely inside a Python virtual environment on WSL
✔️ Code is version-controlled and live on GitHub

---

## 🛠️ Build Process (for beginners)

### 🧱 Step 1: Project Folder

```bash
mkdir nano-llm-doc-qa && cd nano-llm-doc-qa
```

Create these subfolders:

```
app/         # Python logic files
config/      # Settings in YAML format
data/        # Place your PDFs or DOCX files here
chroma_db/   # This will be auto-created to store processed info
```

### 🐍 Step 2: Setup Python Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
```

If `venv` fails, install with:

```bash
sudo apt install python3-venv -y
```

### 📦 Step 3: Install Required Libraries

```bash
pip install chromadb python-docx PyMuPDF streamlit requests pyyaml
```

If any library fails, try `pip install --upgrade package_name`

### 🔑 Step 4: Add API Key (OpenRouter)

Register at: [https://openrouter.ai](https://openrouter.ai)

Then create:

```
config/config.yaml
```

With this content:

```yaml
llm:
  provider: openrouter
  api_key: "sk-...your-key-here..."
  model: "mistralai/mistral-7b-instruct"
```

### 📥 Step 5: Add Documents

Put all your documents in the `data/` folder. Example:

```
data/
└── Genesys Ccaas Guide.pdf
```

### 🧪 Step 6: Ingest Your Docs

```bash
python app/ingest.py
```

You should see:

```
Ingesting: data/Genesys Ccaas Guide.pdf
✅ Ingestion complete!
```

### ❓ Step 7: Ask Questions via CLI

```bash
PYTHONPATH=. python app/test_query.py
```

Edit `test_query.py` and update this line:

```python
question = "What is CCaaS?"
```

### 🌐 Step 8: Launch Web UI

```bash
PYTHONPATH=. streamlit run app/ui_app.py
```

Open browser at: [http://localhost:8501](http://localhost:8501)

Use the chat box to ask questions like:

* "What does Genesys Cloud mean by queue?"
* "Explain CCaaS in simple words."

---

## 📂 Directory Overview

```
nano-llm-doc-qa/
├── app/
│   ├── ingest.py           # Parses and indexes files
│   ├── query_engine.py     # Query logic with ChromaDB + LLM
│   ├── llm_runner.py       # Handles API call to OpenRouter
│   └── test_query.py       # Simple test CLI script
├── config/
│   └── config.yaml         # Your API key and model config
├── data/                   # Your input documents
├── chroma_db/              # Local database folder (auto-created)
├── requirements.txt        # All installable Python packages
├── README.md               # Project documentation
```

---

## 📤 GitHub Integration

### Setup (First Time)

```bash
git init
git remote add origin https://github.com/shanmukhkoya/nano-llm-doc-qa.git
git add .
git commit -m "Initial commit"
git branch -M main
git push -u origin main
```

### Later Updates

```bash
git add .
git commit -m "Update ingestion + fix bugs + working UI"
git push origin main
```

To check if local = GitHub:

```bash
git status
```

You should see:

```
On branch main
Your branch is up to date with 'origin/main'.
```

---

## 🧠 LLM + Tech Stack

* **Python 3.12**
* **ChromaDB** - fast local embedding DB
* **LangChain** - text splitting + RAG pipeline
* **OpenRouter API** - cloud-based LLM (Mistral 7B etc.)
* **Streamlit** - frontend for Q\&A
* **PyMuPDF / python-docx** - for PDF/DOCX reading

---

## 🧪 Test Questions

* "What is CCaaS?"
* "Explain call routing in Genesys Cloud."
* "Where can I access community help?"

---

## 🙌 Maintainer & Learner

Project built step-by-step by **Shanmukh Koya** as a learning project to master:

* Python development
* Document-based AI apps
* Building and deploying local LLM tools
* GitHub + Streamlit + APIs

Feel free to fork, reuse, and improve this project!

---

## 🚀 Coming Soon (Next Phase)

* ✅ File upload from UI
* 🔄 Local LLM options (LLaMA.cpp / GPT4All)
* 💡 More model configurations
* 📦 One-click installer or Docker version
