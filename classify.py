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
    print("Usage: python classify.py 'your question here'")
    sys.exit(1)

question = " ".join(sys.argv[1:])

#bro why is the docs lowkey so confusing
# RAG will come somewhere here at some point but now imma go do the shitty frontend

# engineered system prompt that always gets attached - Ty and Yasmine are working on this as of now
engineered_prompt = """You are a strict text classifier for queries about the World Robot Olympiad (WRO) Robomission event.   

The Robomission event uses LEGO MINDSTORMS or SPIKE Prime robots. 

Teams complete missions on a game mat.   

Questions may involve programming, robot building, competition rules, event logistics, or hardware specifications. 

 

Your task is to classify each query into exactly one category from the list below: 

1. Coding Help (programming logic, errors, sensor use, loops, debugging, block code, etc.) 

2. Mechanical Design Help (building the robot, gears, wheels, attachments, stability, modular design, etc.) 

3. Rules Questions (competition rules, allowed materials, restrictions, task requirements, etc.) 

4. Competition Questions (event logistics, match flow, scoring, timing, practice rounds, etc.) 

5. Technical Specifications (robot dimensions, motor/port limits, sensor compatibility, hardware restrictions, etc.) 

6. Other (anything unrelated to the above, e.g., greetings, off-topic chatter)   

 

Instructions: 

Read the user's query carefully. 

Always choose the single most appropriate category. 

Respond with ONLY the category number (1, 2, 3, 4, or 5). 

If the query does not clearly fit categories 1-5, respond with 6 (other). 

Do not guess. 

Do not include any words, punctuation, explanation, or extra text. 

Do not put any extra characters.  

Examples: 

User: "My color sensor doesn't detect the line properly, what should I do?" 

Answer: 1 

 

User: "Which gear ratio makes my robot faster on the mat?" 

Answer: 2 

 

User: "Can we use tape on the robot to hold parts together?" 

Answer: 3 

 

User: "How many rounds will we get during the tournament?" 

Answer: 4 

 

User: "What is the maximum size of the robot before the start?" 

Answer: 5 

 

User: "Hello coach!" 

Answer: 6 

 

User: “Can I use LEGO string to pull objects?” 

Answer: 2 

 

User: “How many points is touching the blue area worth?” 

Answer: 4 

 

User: “Do we need to document out programming strategy?” 

Answer: 3 

 

User: “My EV3 motor stops working randomly” 

Answer: 5 

 

Now classify this query: 


 
"""

# combine engineered prompt with user input into one string
final_input = engineered_prompt + question

response = client.responses.create(  #this acc to docs at least should mean that im no longer on the old format and hopefully it supports multimodal inputs later on
    model="gpt-5-nano",
    input=final_input,
    max_output_tokens=4000,  # limit output length - so I dont get cooked by the bills
)

#For anyone reading this during developement (prolly tristan or future me). This is the file where we will also get the output back and process to send to the different prompt files
# As in the 1-5 output from gpt will be processed and the and then sent off - I havent added the logic yet because this file wont run in such case

ai_output = response.output_text.strip()
print("AI returned:", ai_output) # for debugging

# try to parse the AI output as an integer between 1 and 5 if its not this is the try catch. 

try:
    choice = int(ai_output)
    if 1 <= choice <= 5:
        script_name = f"script{choice}.py"
        print(f"Calling {script_name}...")
        subprocess.run([sys.executable, script_name, question])  # calls script1.py ... script5.py idk the names yet but this is the play 1 -5 
    else:
        print("AI output was not between 1 and 5.")
except ValueError:
    print("AI output was not a valid integer AKA fix prompt.") 
