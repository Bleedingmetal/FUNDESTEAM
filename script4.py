import sys
import subprocess
from dotenv import load_dotenv
import os




if len(sys.argv) < 2:
    print("Usage: python query.py 'your question here'")
    sys.exit(1)

question = " ".join(sys.argv[1:])

print(question)
