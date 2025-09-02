import sys
from openai import OpenAI
from dotenv import load_dotenv
import os

# load .env so API key is available
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
use_stream = os.getenv("USE_STREAM")
use_stream = os.getenv("USE_STREAM", "false").lower() in ("1", "true", "yes", "on") # set stream mode type to boolean

if not api_key:
    print("OPENAI_API_KEY not found in .env (text aditya so he can setup your key)") #ik ts unecessary but this is for the slow ones 
    sys.exit(1)

client = OpenAI(api_key=api_key)

if len(sys.argv) < 2:
    print("Usage: python query.py 'your question here'")
    sys.exit(1)

question = " ".join(sys.argv[1:])

#bro why is the docs lowkey so confusing
# RAG will come somewhere here at some point but now imma go do the shitty frontend

response = client.responses.create(  #this acc to docs at least should mean that im no longer on the old format and hopefully it supports multimodal inputs later on
    model="gpt-5-nano",
    input=question,
    max_output_tokens=950,  # limit output length - so I dont get cooked by the bills
    stream=use_stream,
)

if use_stream:
    # this code is only valid in stream mode, hence the type ignore
    for event in response:
        if event.type == "response.output_text.delta": # type: ignore
            print(event.delta, end="", flush=True) # type: ignore
else:
    # this code is only valid in non-stream mode, hence the type ignore
    print(response.output_text) # type: ignore