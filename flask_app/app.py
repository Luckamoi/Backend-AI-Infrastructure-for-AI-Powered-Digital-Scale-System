import os
import logging
from flask import Flask, request, jsonify
import requests

# Logging Configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Configuration
OLLAMA_API = os.getenv("OLLAMA_API", "http://host.docker.internal:11434/api/generate")
MODEL_NAME = os.getenv("MODEL_NAME", "llama3.2")

@app.route("/")
def health():
    """Health check endpoint to verify API status."""
    return {"status": "API is operational"}

@app.route('/chat', methods=['POST'])
def chat():
    """
    Endpoint to receive a prompt and forward it to the Ollama API.
    Expected JSON: {"prompt": "your text"}
    """
    data = request.get_json(silent=True)

    if not data or "prompt" not in data:
        return jsonify({"status": "error", "message": "Prompt is required"}), 400

    prompt = data["prompt"]

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    try:
        logger.info(f"Forwarding request to Ollama service using model: {MODEL_NAME}")

        response = requests.post(
            OLLAMA_API,
            json=payload,
            timeout=30
        )
        response.raise_for_status()

        result = response.json()

        return jsonify({
            "status": "success",
            "model": MODEL_NAME,
            "text": result.get("response", "")
        })

    except requests.exceptions.Timeout:
        logger.error("The request to AI service timed out")
        return jsonify({"status": "error", "message": "AI service timeout"}), 504

    except requests.exceptions.RequestException as e:
        logger.error(f"Ollama request failed: {e}")
        return jsonify({
            "status": "error",
            "message": "Failed to connect to AI service",
            "details": str(e)
        }), 500

if __name__ == "__main__":
    # In production, consider using a WSGI server like Gunicorn
    app.run(host="0.0.0.0", port=5000)
    
