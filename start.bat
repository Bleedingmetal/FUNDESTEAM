@echo off
echo ===============================
echo Starting Flask backend...
echo ===============================
start cmd /k "python server.py"

echo ===============================
echo Starting Vite frontend...
echo ===============================
cd chatbot-frontend
start cmd /k "yarn dev"

echo ===============================
echo Both backend and frontend started!
