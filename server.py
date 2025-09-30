from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import sys

app = Flask(__name__)
CORS(app)  # allow requests from frontend

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    try:
        # Run classify.py with the user message
        result = subprocess.run(
            [sys.executable, "classify.py", user_message],
            capture_output=True,
            text=True
        )

        # Split all printed lines
        raw_lines = result.stdout.strip().splitlines()

        # Keep only script output (ignore classify debug)
        script_lines = [
            line for line in raw_lines
            if not (line.startswith("AI returned:") or line.startswith("Calling"))
        ]

        response_text = script_lines[-1] if script_lines else "No response."

        return jsonify({"response": response_text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
