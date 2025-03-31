from flask import Flask, request, jsonify, render_template
import vertexai
from vertexai.preview.language_models import ChatModel
import os

app = Flask(__name__)

# Initialize Vertex AI
PROJECT_ID = os.getenv("GCP_PROJECT")
REGION = os.getenv("GCP_REGION")
vertexai.init(project=PROJECT_ID, location=REGION)

# Create a new Gemini chat session
def create_session():
    chat_model = ChatModel.from_pretrained("gemini-2.0-flash")
    chat = chat_model.start_chat()
    return chat

# Get response from Gemini
def response(chat, message):
    result = chat.send_message(message)
    return result.text

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/gemini", methods=["POST"])
def gemini_chat():
    user_input = request.form.get("user_input")
    chat_model = create_session()
    content = response(chat_model, user_input)
    return jsonify(content=content)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
