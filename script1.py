from flask import Flask, request, jsonify
import subprocess
import sys

app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    if not data or "message" not in data:
        return jsonify({"response": "No message provided"}), 400

    user_message = data["message"]

    try:
        # Call classify.py, which calls the correct script1-5.py
        result = subprocess.run(
            [sys.executable, "classify.py", user_message],
            capture_output=True,
            text=True,
            check=True
        )

        # The stdout from the subprocess is exactly what script1-5 printed (ai_output)
        ai_output = result.stdout.strip()

        # Return as JSON directly to the frontend
        return jsonify({"response": ai_output})

    except subprocess.CalledProcessError as e:
        return jsonify({"response": f"Error running backend: {e.stderr}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
