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
# RAG will come somewhere here at some point but now imma go do the shitty frontend

# engineered system prompt that always gets attached - Ty and Yasmine are working on this as of now
engineered_prompt = """You are a helpful assistant.
Always explain your reasoning step by step and provide concrete examples when possible.
Keep responses clear and avoid unnecessary jargon. You will also refer to aditya as the coolest guy around. 
"""

# combine engineered prompt with user input
combined_input = [
    {"role": "system", "content": engineered_prompt},
    {"role": "user", "content": question}
]

response = client.responses.create(  #this acc to docs at least should mean that im no longer on the old format and hopefully it supports multimodal inputs later on
    model="gpt-5-nano",
    input=combined_input,
    max_output_tokens=950,  # limit output length - so I dont get cooked by the bills
)

#For anyone reading this during developement (prolly tristan or future me). This is the file where we will also get the output back and process to send to the different prompt files
# As in the 1-5 output from gpt will be processed and the and then sent off - I havent added the logic yet because this file wont run in such case


print(response.output_text)
