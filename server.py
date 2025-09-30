# server.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)  # allow frontend requests

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message", "")

        # Run classify.py with the prompt
        # stdout and stderr are captured from the entire process tree
        result = subprocess.run(
            ["python", "classify.py", user_message],
            capture_output=True,
            text=True
        )

        # Check both stdout and stderr (in case child scripts print to stderr)
        output = (result.stdout + "\n" + result.stderr).strip()

        if not output:
            output = "No output from classify.py or its child scripts."

        print("Captured output:", repr(output))  # Debug
        return jsonify({"response": output})

    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
