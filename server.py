# server.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)

# In-memory per-category histories (reset every server restart or frontend reload)
histories = {str(i): [] for i in range(1, 6)}

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message", "")

        # Run classify.py with the user message
        # stdout includes both the category and the script reply
        # Format expected from classify.py:
        #   __CAT__:N
        #   <script reply here>
        result = subprocess.run(
            ["python", "classify.py", user_message],
            capture_output=True,
            text=True
        )

        raw_output = (result.stdout + "\n" + result.stderr).strip()
        if not raw_output:
            return jsonify({"response": "No output from classify.py or its child scripts."})

        # Parse output: first line must start with __CAT__:
        lines = raw_output.splitlines()
        if lines[0].startswith("__CAT__:"):
            category = lines[0].replace("__CAT__:", "").strip()
            reply = "\n".join(lines[1:]).strip()
        else:
            # Fallback if classify.py didn't include category marker
            category = "0"
            reply = raw_output

        # Update history for the chosen category if valid
        if category in histories:
            histories[category].append({"role": "user", "content": user_message})
            histories[category].append({"role": "assistant", "content": reply})

        return jsonify({"response": reply})

    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"}), 500


@app.route("/reset", methods=["POST"])
def reset():
    """Reset all category histories when frontend reloads."""
    global histories
    histories = {str(i): [] for i in range(1, 6)}
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(debug=True)
