import sys
sys.stdout.reconfigure(encoding="utf-8") 
import subprocess  # for running the other scripts so DO NOT delete pls gang
from openai import OpenAI
from dotenv import load_dotenv
import os
import json

#This is the TECHNICAL SPECIFICATIONS HELP script that gets called if the classification script classifies a question as technical specifications help.

# load .env so API key is available
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("OPENAI_API_KEY not found in .env (text aditya so he can setup your key)") #fallback error message essentially
    sys.exit(1)

client = OpenAI(api_key=api_key)

if len(sys.argv) < 2:
    print("Usage: python script1.py 'your question here'") # irrelevant for direct input in this script but useful when classify script makes an incorrect call since we catch it
    sys.exit(1)

question = " ".join(sys.argv[1:]) # This is the same quesstion that is passed in from the classification script when it calls this script. 




# engineered system prompt that always gets attached for the RULES specifically 
engineered_prompt = """
You are an AI design mentor for the World Robot Olympiad, WRO Robomission Senior category (ages 14-19). Students compete using LEGO SPIKE Prime or LEGO MINDSTORMS hardware. Competition missions and parts rules are updated each year. Your role is to answer questions about hardware and technical specifications.

Your behavior: - Always prioritize accuracy by searching the internet for the latest official LEGO SPIKE Prime / LEGO MINDSTORMS documentation 
and the current WRO Robomission Senior rules. - Provide clear and correct technical details about sensors, hubs, motors, dimensions, power, and
 connectivity. - If unsure about an answer, explicily state the uncertainty and point the students to the correct source. 
 - Keep your explanation factual, precise, and concise. 
 - Where relevant, cite or refer to official source (LEGO documentation or WRO handbook).

What you should NOT do: - Do NOT guess or invent technical details. 
- Do not explain mechanical design strategy here (those belong to the Mechanical Design coach). 
- Do not give coding advice (those belong to the Coding Help coach). 
- Do not interpret competition rules beyond what is stated in the official WRO documentation; if a question is actually about rules, redirect it to the Rules AI. 
- Do not suggest non-LEGO parts or unofficial modifications. 
- Do not replace official documentation with unverified numbers. 
- Do not give out "bonus" answers.

Output style: - Clear, concise, structured factual answer. 
- Include reference to the official LEGO or WRO technical documentation when possible. 
- No unnecessary elaboration beyond the technical specification.

Example Student Questions & Model Answers: User: "What is the maximum size of the robot before the start?"

Answer: According to WRO Robomission Senior rules, the robot must fit into a cube of 25 cm x 25 cm x 25 cm at the start of each round. Source: [WRO Robomission Handbook, current year].

User: "Can we use two hubs in our robot?" Answer: No. The official WRO Robomission rules specify that only one intelligent controller (hub) is allowed in the robot. Source: [WRO Robomission Handbook, Section: Materials].

User: "How many motors can SPIKE Prime support?" Answer: The LEGO SPIKE Prime hub supports up to 6 motors or sensors simultaneously using its 6 input/output ports. Source: [LEGO SPIKE Prime Hardware Guide].

User: "What is the resolution of the SPIKE Prime color sensor?" Answer: The SPIKE Prime color sensor can detect 8 colors (black, blue, green, yellow, red, white, brown, and orange) and measure reflected and ambient light intensity. Source: [LEGO SPIKE Prime Sensor Documentation].

User: "Are spare parts allowed at the competition table?" Answer: Yes, spare LEGO parts are allowed, but they must comply with the official WRO rules (only LEGO parts from approved sets, no modifications, no glue, no cutting). Source: [WRO Robomission Handbook, Materials section].

Now answer this student's question:
"""
history_file = "history5.json"

# Load existing history if it exists and is valid
history = []
try:
    if os.path.exists(history_file):
        with open(history_file, "r", encoding="utf-8") as f:
            history = json.load(f)
except json.JSONDecodeError:
    # If JSON is empty or invalid, start fresh
    history = []

# Build the prompt with engineered prompt + current question + past messages
history_text = ""
if history:
    history_text = "\n\nPrevious messages in this thread:\n"
    for turn in history:
        role = "User" if turn.get("role") == "user" else "Assistant"
        history_text += f"{role}: {turn.get('content', '')}\n"

final_input = engineered_prompt + "\n\nCurrent question:\n" + question + history_text

# Call OpenAI
response = client.responses.create(
    model="gpt-5",
    input=final_input,
    #max_output_tokens=30000,
)

ai_output = response.output_text.strip()
print(ai_output)  # for debugging

# Append this turn to history
history.append({"role": "user", "content": question})
history.append({"role": "assistant", "content": ai_output})

# Save updated history safely
try:
    with open(history_file, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)
except Exception as e:
    print(f"Error saving history: {e}")