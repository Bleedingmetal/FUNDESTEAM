# FUNDESTEAM Assistant

This project is an AI-powered chatbot with:

- **Frontend**: React (Vite + TypeScript + TailwindCSS)  
- **Backend**: Python scripts powered by the OpenAI API  

At this stage:  
- The **backend** runs standalone (via `classify.py`) instead of as a web server.  
- The **frontend** is a chat-like interface (not yet connected to the backend).  

---

##  Quick Start

- **Frontend**:  
  ```bash
  cd chatbot-frontend
  yarn install
  yarn dev

- **Backend**:
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
pip install -r requirements.txt
echo "OPENAI_API_KEY=your_api_key_here" > .env
python classify.py "Can we use tape on the robot?"

