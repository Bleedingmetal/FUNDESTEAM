from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import subprocess
import os

app = Flask(__name__, static_folder="static")
CORS(app)

# In-memory per-category histories
histories = {str(i): [] for i in range(1, 6)}

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message", "")

        # Run classify.py
        result = subprocess.run(
            ["python", "classify.py", user_message],
            capture_output=True,
            text=True
        )

        raw_output = (result.stdout + "\n" + result.stderr).strip()
        if not raw_output:
            return jsonify({"response": "No output from classify.py or its child scripts."})

        lines = raw_output.splitlines()
        if lines[0].startswith("__CAT__:"):
            category = lines[0].replace("__CAT__:", "").strip()
            reply = "\n".join(lines[1:]).strip()
        else:
            category = "0"
            reply = raw_output

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
    global histories
    histories = {str(i): [] for i in range(1, 6)}

    # Delete per-script history JSON files
    for i in range(1, 6):
        path = f"history{i}.json"
        if os.path.exists(path):
            os.remove(path)

    return jsonify({"status": "ok"})

# Serve React frontend
@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve_frontend(path):
    if path != "" and os.path.exists(os.path.join("static", path)):
        return send_from_directory("static", path)
    return send_from_directory("static", "index.html")

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8000)
