import os
import logging
from flask import Flask, request, jsonify
import requests

# Logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Config
OLLAMA_API = os.getenv("OLLAMA_API", "http://host.docker.internal:11434/api/generate")
MODEL_NAME = os.getenv("MODEL_NAME", "llama3.2")

@app.route("/")
def health():
    return {"status": "API running"}

@app.route('/chat', methods=['POST'])
def chat():
    """
    Endpoint สำหรับรับ Prompt และส่งต่อไปยัง Ollama API
    Expected JSON: {"prompt": "your text"}
    """
    data = request.get_json(silent=True)

    if not data or "prompt" not in data:
        return jsonify({"error": "Prompt is required"}), 400

    prompt = data["prompt"]

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    try:
        logger.info(f"Sending request to Ollama ({MODEL_NAME})")

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
        logger.error("Request timed out")
        return jsonify({"error": "AI service timeout"}), 504

    except requests.exceptions.RequestException as e:
        logger.error(f"Ollama request failed: {e}")
        return jsonify({
            "error": "Failed to connect to AI service",
            "details": str(e)
        }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
