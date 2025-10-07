# FUNDESTEAM Chatbot

An AI-powered tutoring assistant built with **React + TypeScript (Vite)** on the frontend and **Python + Flask** on the backend. The chatbot is designed to help students prepare for and learn concepts related to the **WRO (World Robot Olympiad)** competition.

This guide provides both a **Quick Setup** for experienced users and a **Full Beginner Setup** for those with no technical background.

---

## System Requirements

* **Operating System:** Windows 10/11 (macOS/Linux supported with minor path adjustments)
* **Processor:** Dual-core or better
* **Memory:** 4 GB minimum (8 GB recommended)
* **Storage:** At least 2 GB free space
* **Internet:** Required for downloading dependencies and using the OpenAI API

---

## Quick Setup (for experienced users)

If you already have **Python 3.10.0**, **Node.js 24.7.0**, and **Yarn 4.9.1** installed:

```bash
git clone https://github.com/Bleedingmetal/FUNDESTEAM.git
cd FUNDESTEAM
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate on macOS/Linux
pip install -r requirements.txt
mv .env.example .env  # add your OpenAI API key here
cd chatbot-frontend
yarn install
yarn dev  # frontend
yarn dev  # frontend in one terminal
python server.py  # backend in another terminal
```

To run both together on Windows:

```bash
start.bat
```

---

## Full Detailed Setup (for beginners)

### 1. Required Tools

You will need:

* **Visual Studio Code** &ndash; for running and editing code
* **Git** &ndash; for downloading the project
* **Python 3.10.0** &ndash; backend runtime
* **Node.js 24.7.0** &ndash; frontend runtime
* **Yarn 4.9.1** &ndash; frontend package manager

All instructions below assume Windows. For macOS/Linux, replace paths accordingly.

---

### 2. Install Visual Studio Code

1. Visit [https://code.visualstudio.com/](https://code.visualstudio.com/)
2. Download and install using all default settings.
3. Launch VS Code once done.

---

### 3. Install Git

1. Go to [https://git-scm.com/downloads](https://git-scm.com/downloads)
2. Download and install (keep defaults).
3. Open **Command Prompt** and verify:

   ```bash
   git --version
   ```

   Expected output: `git version 2.x.x`

---

### 4. Clone the Repository

1. Open Command Prompt.
2. Navigate to your desired folder, e.g.:

   ```bash
   cd Desktop
   ```
3. Clone the project:

   ```bash
   git clone https://github.com/Bleedingmetal/FUNDESTEAM.git
   ```
4. Open VS Code &rarr; File &rarr; Open Folder &rarr; select **FUNDESTEAM**

---

### 5. Install Python 3.10.0

1. Go to [https://www.python.org/downloads/release/python-3100/](https://www.python.org/downloads/release/python-3100/)
2. Download and install.
3. **Important:** Check *Add Python to PATH*.
4. Verify:

   ```bash
   python --version
   ```

   Expected: `Python 3.10.0`

---

### 6. Set Up the Backend

1. In VS Code, open a terminal (**Ctrl + `** or accesible from the navbar above).

2. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

3. Activate it:

   * **Windows:** `venv\Scripts\activate`
   * **macOS/Linux:** `source venv/bin/activate`

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Configure environment variables:

   * You already have `.env.example` in the project.
   * Rename it to `.env` and add your OpenAI API key:

     ```
     OPENAI_API_KEY=your_api_key_here
     ```

Backend setup is complete.

---

### 7. Install Node.js 24.7.0

1. Go to [https://nodejs.org/en/download](https://nodejs.org/en/download)
2. Install **Node.js 24.7.0 (Current)** with defaults.
3. Verify:

   ```bash
   node -v
   ```

   Expected: `v24.7.0`

---

### 8. Install Yarn 4.9.1

1. Enable Corepack (included with Node):

   ```bash
   corepack enable
   ```
2. Set Yarn version:

   ```bash
   corepack prepare yarn@4.9.1 --activate
   ```
3. Verify:

   ```bash
   yarn -v
   ```

   Expected: `4.9.1`

---

### 9. Set Up the Frontend

1. In VS Code, open a new terminal.
2. Move to the frontend folder:

   ```bash
   cd chatbot-frontend
   ```
3. Install dependencies:

   ```bash
   yarn install
   ```

---

### 10. Running the Chatbot

#### Option A: Run Separately

**Backend:**

```bash
python server.py
```

Expected message:

```
Running on http://127.0.0.1:5000
```

**Frontend:**

```bash
cd chatbot-frontend
yarn dev
```

Expected message:

```
Local: http://localhost:3000/
```

Visit `http://localhost:3000` in your browser.

#### Option B: Run Both Together (Windows Only)

Double-click **start.bat** in the root directory or run:

```bash
start.bat
```

This will start both servers automatically.

---

### 11. Testing the Backend

To test the backend directly:

```bash
python classify.py "How does a PID loop work?"
```

You should see a text-based AI response printed to the terminal.

---

### 12. Folder Structure

```
FUNDESTEAM/
│
├── chatbot-frontend/         # React + Vite frontend
│   ├── src/                  # Frontend code
│   ├── package.json          # Frontend dependencies
│   ├── vite.config.ts        # Vite config
│   ├── yarn.lock             # Yarn lock file
│   └── ...                   # Other frontend files
│
├── server.py                 # Flask backend
├── classify.py               # GPT-powered classification
├── requirements.txt          # Python dependencies
├── .env.example              # Example environment file
├── start.bat                 # Combined start script (Windows)
└── README.md                 # This documentation
```

---

### 13. Troubleshooting

**Problem:** `'python' is not recognized`

* **Fix:** Reinstall Python and enable *Add to PATH*.

**Problem:** `'yarn' is not recognized`

* **Fix:**

  ```bash
  corepack enable
  corepack prepare yarn@4.9.1 --activate
  ```

**Problem:** Frontend cannot connect to backend.

* **Fix:** Ensure both servers are running.

  * Backend → `http://localhost:5000`
  * Frontend → `http://localhost:3000`

**Problem:** OpenAI key not working.

* **Fix:** Check `.env` file for a valid `OPENAI_API_KEY`.

---

### 14. Stopping the Servers

Press `Ctrl + C` in any terminal running the app.

---

### 15. Completion

You now have the **FUNDESTEAM Chatbot** fully configured and running — a complete tutor for helping students learn and prepare for the WRO competition.

---
### 16. Common Questions for Beginners

**Q: Do I need administrator rights to install Python, Node.js, or Git?**

A: Usually not, but some Windows setups may ask for admin permission. If prompted, click “Yes” to continue installation.

**Q: What if my Python version is different from 3.10.0?**

A: The chatbot is tested with Python 3.10.0. Later versions *might* work, but if you run into errors, install 3.10.0 to match the guide.

**Q: Do I have to install exactly Node.js 24.7.0 and Yarn 4.9.1?**

A: These versions are recommended to avoid compatibility issues. Other versions *might* work, but the commands and scripts are verified for these exact versions.

**Q: What if port 3000 or 5000 is already in use?**

A: You’ll need to free the port or change the frontend/backend port. For example:

* Frontend: `vite --port 3001`
* Backend: edit `server.py` &rarr; `app.run(port=5001)`

**Q: How do I add my OpenAI API key correctly?**

A: Rename `.env.example` to `.env` and replace the placeholder with your key like this:

```
OPENAI_API_KEY=your_api_key_here
```

**Q: The chatbot doesn’t respond in the frontend—what should I check?**
A: Make sure:

1. The backend is running (`python server.py`)
2. The frontend is running (`yarn dev`)
3. Your `.env` has a valid API key

**Q: Can I run this on macOS or Linux?**
A: Yes! Paths for activating the virtual environment differ:

* macOS/Linux: `source venv/bin/activate`
* Windows: `venv\Scripts\activate`

**Q: How do I stop the chatbot?**
A: Press `Ctrl + C` in any terminal running the app. Both frontend and backend servers will stop.

> **Tip for beginners:** Don’t worry if this seems complicated at first &ndash; just follow each step carefully and you’ll have the chatbot running in under 30 minutes!

---

### Author

**BleedingMetal**

[GitHub Repository](https://github.com/Bleedingmetal/FUNDESTEAM)

---

### License (MIT)

Copyright (c) 2025 BleedingMetal

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
