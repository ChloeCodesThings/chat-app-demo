# 🤖💬 Gemini Chat App on Cloud Run

You can check out the blog here! (LINK COMING SOON!)

This is a simple Flask web app that lets users chat with Google's Gemini LLM (Large Language Model). The app runs on Google Cloud Run, uses Vertex AI for the Gemini API, and is containerized with Docker.

## 🧠 What It Does

- Accepts user input through a web form
- Sends that input to Gemini via Vertex AI's Python SDK
- Displays the model's response in a chat-like UI

## 🛠️ Technologies Used

- [Flask](https://flask.palletsprojects.com/) – Lightweight web framework
- [Vertex AI SDK](https://cloud.google.com/vertex-ai/docs/start/client-libraries) – To interact with the Gemini API
- [Cloud Run](https://cloud.google.com/run) – For serverless container deployment
- [Artifact Registry](https://cloud.google.com/artifact-registry) + [Cloud Build](https://cloud.google.com/build) – For container builds and storage

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- Docker
- A Google Cloud project with:
  - Vertex AI API enabled
  - Billing enabled
  - Cloud SDK (`gcloud`) authenticated

### 1. Clone this repo

`git clone https://github.com/YOUR_USERNAME/chat-gemini-cloudrun.git
cd chat-gemini-cloudrun`

### 2. Install Python dependencies

`pip install -r requirements.txt`

### 3. Run locally
Make sure to set the following environment variables first:
`export GCP_PROJECT=your-project-id
export GCP_REGION=your-region`

Then start the app:
`python app.py`

Visit http://localhost:8080 in your browser.

### 🐳 Build and Deploy with Cloud Run

(coming soon!)



