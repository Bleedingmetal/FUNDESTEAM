import sys
# from openai import OpenAI
from dotenv import load_dotenv
import os
import ollama

# use predefined ollama model or select at runtime (for testing only)
prefer_env_model = True # default: True

# load .env to pick ollama model
load_dotenv()
ollama_model = os.getenv("OLLAMA_MODEL")

# if no argument is provided, print usage and exit
if len(sys.argv) < 2:
    print("Usage: python query.py 'your question here'")
    sys.exit(1)

# list ollama models
models = sorted(ollama.list()["models"], key=lambda m: m["model"])

if not models:
    print("No Ollama models installed. Run 'ollama pull <model>' first.")
    sys.exit(1)

model_names = [m["model"] for m in models]

# if no ollama model is set, ask the user to select one
if not prefer_env_model:
    for i, m in enumerate(models, start=1):
        size_gb = round(m["size"] / (1024**3), 2)
        parameter_size = m["details"]["parameter_size"]
        print(f"{i}. {m['model']}  ({parameter_size} parameters, {size_gb:.2f} GB)")

    choice = input("\nEnter the number corresponding to the model you want to use: ")

    try:
        selected_model = models[int(choice) - 1]["model"]
    except (ValueError, IndexError):
        print("Invalid selection.")
        sys.exit(2)
        
# use ollama model set in .env if user chooses to
else:
    # if no ollama model is set in .env, exit
    if not ollama_model:
        print("No OLLAMA_MODEL set in .env")
        sys.exit(1)
    # if ollama model is set in .env, check if it's valid
    if not ollama_model in model_names:
        print(f"Invalid OLLAMA_MODEL in .env: '{ollama_model}'")
        print(f"If this is a valid model name, you may have forgotten to install it with 'ollama pull {ollama_model}'")
        sys.exit(1)

    selected_model = ollama_model

# create prompt content
question = " ".join(sys.argv[1:])

stream = ollama.chat(
    model=selected_model,
    messages=[{"role": "user", "content": question}],
    stream=True,
)

for chunk in stream:
    print(chunk["message"]["content"], end="", flush=True)
