# 🐳 Containerizing Steps of nano-llm-doc-qa App (`nano-llm-doc-qa`)

This guide helps you containerize your **Nano LLM Document QA** Streamlit app using Docker — enabling portable deployment and consistent environments across machines.

---

## 📋 Table of Contents

1. [Prerequisites: Installing Docker](#prerequisites-installing-docker)
2. [Dockerfile](#dockerfile)
3. [.dockerignore File](#dockerignore-file)
4. [Build and Run Instructions](#build-and-run-instructions)

---

## ✅ Prerequisites: Installing Docker

### On Windows

* Install **Docker Desktop** from:
  👉 [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)
* Ensure **WSL 2 backend** is enabled (Docker Desktop prompts you during setup).

### On Linux (Ubuntu/Debian-based)

Run the following in terminal:

```bash
sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates curl gnupg lsb-release
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] \
https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | \
sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io

# Verify Docker is working
sudo docker run hello-world
```

---

## 🛠 Dockerfile

Create a file named `Dockerfile` in the **`nano-llm-doc-qa/`** root directory:

```Dockerfile
# Use a slim Python base image
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

# Expose Streamlit's default port
EXPOSE 8501

# Start the Streamlit app (update script name if needed)
CMD ["streamlit", "run", "app.py"]
```

---

## 🚫 .dockerignore File

Create a `.dockerignore` file in **`nano-llm-doc-qa/`** to exclude unnecessary files from the Docker image:

```dockerignore
# Git
.git
.gitignore

# Docker
Dockerfile
.dockerignore

# Python
venv/
.venv/
__pycache__/
*.py[cod]

# IDE/editor config
.vscode/
.idea/
```

---

## 🚀 Build and Run Instructions

### 1. **Build the Docker Image**

From your project root:

```bash
cd nano-llm-doc-qa
docker build -t nano-llm-qa .
```

### 2. **Run the Docker Container**

```bash
docker run -p 8501:8501 nano-llm-qa
```

### 3. **Open the App in Browser**

Go to:
👉 http://localhost:8501

---

### ✅ Summary

* 📦 Uses `python:3.12-slim` for a minimal image
* 🧼 Clean `.dockerignore` avoids unnecessary files
* ⚡ Simple 2-step build & run process
* 🌐 App accessible at `http://localhost:8501`

Let me know if you'd like next steps such as Docker Compose support, cloud deployment, or CI/CD integration.
