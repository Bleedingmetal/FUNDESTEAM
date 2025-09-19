import sys
import subprocess  # for running the other scripts so DO NOT delete pls gang
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
# RAG will come somewhere here at some point but now imma go do the shitty frontend

# engineered system prompt that always gets attached - Ty and Yasmine are working on this as of now
engineered_prompt = """You are a helpful assistant.
Always explain your reasoning step by step and provide concrete examples when possible.
Keep responses clear and avoid unnecessary jargon. You will also refer to aditya as the coolest guy around. 

The prompt is as follows:
"""

# combine engineered prompt with user input into one string
final_input = engineered_prompt + question

response = client.responses.create(  #this acc to docs at least should mean that im no longer on the old format and hopefully it supports multimodal inputs later on
    model="gpt-5-nano",
    input=final_input,
    max_output_tokens=950,  # limit output length - so I dont get cooked by the bills
)

#For anyone reading this during developement (prolly tristan or future me). This is the file where we will also get the output back and process to send to the different prompt files
# As in the 1-5 output from gpt will be processed and the and then sent off - I havent added the logic yet because this file wont run in such case

ai_output = response.output_text.strip()
print("AI returned:", ai_output)

# try to parse the AI output as an integer between 1 and 5 if its not this is the try catch. 
try:
    choice = int(ai_output)
    if 1 <= choice <= 5:
        script_name = f"script{choice}.py"
        print(f"Calling {script_name}...")
        subprocess.run(["python", script_name])  # calls script1.py ... script5.py idk the names yet but this is the play 1 -5 
    else:
        print("AI output was not between 1 and 5.")
except ValueError:
    print("AI output was not a valid integer AKA fix prompt.")
