# server.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import json

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
        result = subprocess.run(
            ["python", "classify.py", user_message],
            capture_output=True,
            text=True
        )

        raw_output = (result.stdout + "\n" + result.stderr).strip()
        if not raw_output:
            return jsonify({"response": "No output from classify.py or its child scripts."})

        # Expect first line to be __CAT__:N
        lines = raw_output.splitlines()
        if lines[0].startswith("__CAT__:"):
            category = lines[0].replace("__CAT__:", "").strip()
            reply = "\n".join(lines[1:]).strip()
        else:
            category = "0"
            reply = raw_output

        # Update history for the chosen category if valid
        if category in histories:
            histories[category].append({"role": "user", "content": user_message})
            histories[category].append({"role": "assistant", "content": reply})

        return jsonify({
            "response": reply,
            "category": category,
            "history": histories.get(category, [])
        })

    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"}), 500

@app.route("/reset", methods=["POST"])
def reset():
    """Reset all category histories when frontend reloads."""
    global histories
    histories = {str(i): [] for i in range(1, 6)}

    # Delete per-script history JSON files
    for i in range(1, 6):
        path = f"history{i}.json"
        if os.path.exists(path):
            os.remove(path)

    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(debug=True)
