from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import openai
import os
import uuid
import json
import re
from datetime import datetime
from google.cloud import texttospeech
from google.oauth2 import service_account

app = Flask(__name__)
CORS(app)

# Initialize OpenAI client
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load Google Cloud TTS credentials from service account file
credentials = service_account.Credentials.from_service_account_file("lumina-voice-ai.json")
tts_client = texttospeech.TextToSpeechClient(credentials=credentials)

MEMORY_FILE = "memory.json"
user_sessions = {}

# TODO: Add any additional Flask routes, logic, or APIs here.

if __name__ == "__main__":
    app.run(debug=True)
