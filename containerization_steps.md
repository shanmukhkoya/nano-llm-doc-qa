This guide provides all the necessary components to containerize your Python-based Streamlit application, from installation to execution.1. Prerequisites: Installing DockerBefore you can build and run the container, you need to have Docker installed on your system.On WindowsDocker Desktop: The easiest way to get Docker on Windows is by installing Docker Desktop.WSL 2 (Windows Subsystem for Linux): Docker Desktop for Windows uses WSL 2 as its backend. The installer will typically prompt you to enable it if it's not already. It's a good idea to ensure your Windows 10 or 11 is up-to-date to support WSL 2.Download Link: You can download Docker Desktop from the official Docker website: https://www.docker.com/products/docker-desktop/On Linux (Ubuntu/Debian-based)For most Debian-based distributions like Ubuntu, you can install Docker Engine using the following commands in your terminal.Update your package list:sudo apt-get update
Install necessary packages to allow apt to use a repository over HTTPS:sudo apt-get install apt-transport-https ca-certificates curl gnupg lsb-release
Add Docker’s official GPG key:curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
Set up the stable repository:echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
Install Docker Engine:sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
Verify Installation: Check that Docker is installed correctly by running the "hello-world" image.sudo docker run hello-world
For other Linux distributions, please refer to the official Docker documentation.2. DockerfileThis file contains the instructions to build your Docker image. It starts with a base Python image, sets up the environment, installs your dependencies, copies your code, and defines the command to run your application.Create a file named Dockerfile (with no file extension) in the root directory of your project and add the following content:# Use an official Python runtime as a parent image.
# Using python:3.12-slim is a good choice to keep the image size small.
FROM python:3.12-slim

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the requirements file into the container at /app
# This is done first to leverage Docker's layer caching. If requirements.txt
# doesn't change, Docker won't re-install the packages on subsequent builds.
COPY requirements.txt .

# Install pip and the dependencies from requirements.txt
# Using --no-cache-dir reduces the image size.
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application's source code into the container
COPY . .

# Let Docker know that the container listens on port 8501
# This is the default port for Streamlit applications.
EXPOSE 8501

# Define the command to run when the container starts.
# This command starts the Streamlit application.
# IMPORTANT: Replace 'app.py' with the actual name of your main Streamlit script.
CMD ["streamlit", "run", "app.py"]
3. .dockerignore FileThis file tells Docker which files and folders to exclude from the container. This is crucial for keeping your image lightweight and for preventing sensitive files from being included.Create a file named .dockerignore in your project's root directory with this content:# Ignore Git-related files and directories
.git
.gitignore

# Ignore Docker-related files
Dockerfile
.dockerignore

# Ignore Python virtual environments and cache files
venv/
.venv/
__pycache__/
*.pyc
*.pyo
*.pyd

# Ignore common IDE/editor configuration directories
.idea/
.vscode/
4. How to Build and RunWith both files in place, you can now build your image and run your container.Open a terminal or command prompt and navigate to the root directory of your project.Build the Docker image using the docker build command. We'll tag (-t) the image as nano-llm-qa. The . at the end tells Docker to look for the Dockerfile in the current directory.docker build -t nano-llm-qa .
Run the Docker container from the image you just created. The -p flag maps your local machine's port 8501 to the container's port 8501.docker run -p 8501:8501 nano-llm-qa
Access your application by opening your web browser and navigating to: http://localhost:85015. How to Save as PDFYou can easily save a copy of this guide as a PDF file directly from your web browser.Click anywhere inside this document.Press Ctrl+P (on Windows/Linux) or Cmd+P (on Mac) to open the browser's print dialog.In the "Destination" or "Printer" dropdown menu, select "Save as PDF".Click the "Save" button and choose where you want to save the file.
