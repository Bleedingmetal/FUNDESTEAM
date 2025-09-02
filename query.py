import sys
from openai import OpenAI
from dotenv import load_dotenv
import os

# load .env so API key is available
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")


if not api_key:
    print("OPENAI_API_KEY not found in .env (text aditya so he can setup your key)") #ik ts unecessary but this is for the slow ones 
    sys.exit(1)

client = OpenAI(api_key=api_key)

if len(sys.argv) < 2:
    print("Usage: python query.py 'your question here'")
    sys.exit(1)

question = " ".join(sys.argv[1:])

#bro why is the docs lowkey so confusing

response = client.responses.create(  #this acc to docs at least should mean that im no longer on the old format and hopefully it supports multimodal inputs later on
    model="gpt-5-nano",
    input=question,
)

print(response.output_text)
