# FUNDESTEAM Chatbot

An AI-powered tutoring assistant built with **React + TypeScript (Vite)** on the frontend and **Python + Flask** on the backend. The chatbot is designed to help students prepare for and learn concepts related to the **WRO (World Robot Olympiad)** competition.

This guide provides both a **Quick Setup** for experienced users and a **Full Beginner Setup** for those with no technical background.

---
### Table of Contents

1. [System Requirements](#1-system-requirements)
2. [Quick Setup for Experienced Users](#2-quick-setup-for-experienced-users)
3. [Full Detailed Setup for Beginners](#3-full-detailed-setup-for-beginners)
   - [1. Required Tools](#1-required-tools)
   - [2. Install Visual Studio Code](#2-install-visual-studio-code)
   - [3. Install Node.js](#3-install-nodejs)
   - [4. Clone Repository](#4-clone-repository)
4. [Backend Setup](#4-backend-setup)
5. [Frontend Setup](#5-frontend-setup)
6. [Environment Variables](#6-environment-variables)
7. [Running the Backend](#7-running-the-backend)
8. [Running the Frontend](#8-running-the-frontend)
9. [Project Structure](#9-project-structure)
10. [Common Errors and Fixes](#10-common-errors-and-fixes)
11. [Interacting with the Chatbot](#11-interacting-with-the-chatbot)
12. [Updating the Code](#12-updating-the-code)
13. [Adding a New Script](#13-adding-a-new-script)
14. [Testing a Category Independently](#14-testing-a-category-independently)
15. [Configuring Classify.py](#15-configuring-classifypy)
16. [Frontend Features](#16-frontend-features)
17. [Adding a New Category](#17-adding-a-new-category)
---
### Advanced Backend Guidelines
18. [Best Practices for Prompt Writing](#18-best-practices-for-prompt-writing)
19. [Testing and Debugging](#19-testing-and-debugging)
20. [Integrating RAG or External Docs](#20-integrating-rag-or-external-docs)
21. [Security and API Considerations](#21-security-and-api-considerations)
22. [GitHub Workflow](#22-github-workflow)
23. [License](#23-license)
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

  * Backend &rarr; `http://localhost:5000`
  * Frontend &rarr; `http://localhost:3000`

**Problem:** OpenAI key not working.

* **Fix:** Check `.env` file for a valid `OPENAI_API_KEY`.

---

### 14. Stopping the Servers

Press `Ctrl + C` in any terminal running the app.

---

### 15. Completion

You now have the **FUNDESTEAM Chatbot** fully configured and running &mdash; a complete tutor for helping students learn and prepare for the WRO competition.

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

   If you would like to free the port open task manager by hitting `Ctrl + Shift + Esc` search for a *Node.js* task that is running. Select this task and End Task. 
   > Note: There may be multiple Node.js tasks running simultaniously. In such a case, end all these tasks.

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
### 17. Adding a New Category 

You can add new categories to the chatbot by creating a new script (`script9.py`) and updating `classify.py` so the AI can route questions correctly.

### Step A: Create `script9.py`

Copy an existing script (like `script1.py`) and rename it:

```bash
cp script1.py script9.py
```

Inside `script9.py`:

1. Change the `engineered_prompt` to describe the new category.
2. Update the history file name:

```python
# Old line in script1.py
history_file = "history1.json"

# New line in script9.py
history_file = "history9.json"
```

3. Update examples or instructions in the prompt to match the new category focus.

### Step B: Update `classify.py` to Handle Script 9

Find this block in `classify.py` (near the bottom where other scripts are called):

```python
if 1 <= choice <= 5:
    script_name = f"script{choice}.py"
    result = subprocess.run([sys.executable, script_name, question], capture_output=True, text=True)
    script_reply = (result.stdout + "\n" + result.stderr).strip()
    print(f"__CAT__:{choice}")
    print(script_reply)
```

Add the new category handling **directly below it**:

```python
elif choice == 9:
    script_name = "script9.py"
    result = subprocess.run([sys.executable, script_name, question], capture_output=True, text=True)
    script_reply = (result.stdout + "\n" + result.stderr).strip()
    print(f"__CAT__:9")
    print(script_reply)
```

### Step C: Add the Category to `engineered_prompt`

Inside `classify.py`, find the numbered category list in `engineered_prompt` and add your new category:

```python
# Example of existing list
5. Technical Specifications (robot dimensions, motor/port limits, sensor compatibility, hardware restrictions, etc.)

# Add below
9. New Category Name (description of what this category covers)
```

This ensures the classifier knows about the new category when returning numbers.

### Step D: Testing the New Category

To test `script9.py` directly:

```bash
python script9.py "Your test question for the new category"
```

* This runs the script standalone.
* Verify it returns the expected AI output and updates `history9.json` correctly.

### Step E: Scaling for More Categories

If you want to add more in the future, copy the pattern:

```python
elif choice == 6:
    script_name = "script6.py"
    result = subprocess.run([sys.executable, script_name, question], capture_output=True, text=True)
    script_reply = (result.stdout + "\n" + result.stderr).strip()
    print(f"__CAT__:6")
    print(script_reply)
```

* Change the number and script filename for each new category.
* Always add the description in `engineered_prompt` so the AI knows about the new category.

--- 
### 18. Best Practices for Prompt Writing

When writing or adjusting the `engineered_prompt` in `classify.py` or category scripts (`script1-5`, `script9.py`), following these best practices ensures consistent and accurate classification and AI responses.

### A. Adjusting `engineered_prompt` Effectively

* Always start the prompt with a clear description of the AI’s role, e.g., "You are an AI mentor for .... (Your specifc catagory)."
* Explicitly define the purpose of the category and what type of questions should be handled.
* Maintain a concise but complete explanation of what the AI should and should not do.
* Include output formatting instructions (e.g., return numbers only, structured answers, use of Markdown code blocks).
* Avoid ambiguous wording. For example, instead of saying "Answer clearly," specify "Return step-by-step reasoning in plain text and use triple backticks for code blocks."

### B. Guidelines on Example Formatting, Language Style, and Clarity

* Provide concrete examples for both input and expected output, formatted like:

```text
User: "How do I make the robot follow a line?"
Answer: Step-by-step reasoning or pseudocode. Only provide Python code if explicitly asked.
```

* Keep language consistent across examples and scripts.
* Ensure examples reflect the specific category (do not mix coding and mechanical examples).
* Use accented letters for Spanish as needed. Avoid other special Unicode characters.

### C. Avoiding Classifier Confusion

* Make sure new categories added to `engineered_prompt` match exactly the number used in `classify.py` (e.g., 9 &rarr; script9.py).
* Explicitly describe what kinds of questions should go to the new category, so the AI can confidently select it.
>**Important: Do not reuse numbers reserved for debugging (6, 7, 8).**

---
### *Advanced Backend Guidlines*
---

### 19. Testing and Debugging

Proper testing ensures your classifier and scripts behave as expected.

### A. Debugging Classifier Issues

1. **Check last_script.json** &ndash; this stores the last script number when AI returns ambiguous (7) results.
2. **Check script-specific history files** &ndash; e.g., `history1.json`, `history9.json`. Ensure the AI’s responses are correctly appended.
3. **Print AI outputs** &ndash; in `classify.py` or the category script, temporarily add:

```python
print("DEBUG AI OUTPUT:", ai_output)
```

4. **Verify category routing** &ndash; make sure `print(f"__CAT__:{choice}")` is returning the expected number.

### B. Viewing OpenAI API Responses

* Set `debug=True` (if you implement a debug flag) or directly print the raw response:

```python
response = client.responses.create(model="gpt-5-nano", input=final_input)
print(response)
```

* Check the text returned by `response.output_text` to ensure it matches your expectations.

### C. Handling Accented Letters and Special Characters

* Spanish accents are supported in both input and output.
* Avoid using unusual Unicode symbols in prompts (like fancy dashes, emojis, arrows). Use Markdown entities instead, e.g., `&rarr;`, `%endash;`.
* ***Only basic punctuation and letters are guaranteed to work across all scripts.***

---

### 20. Adding Special Characters Support

If you must handle prompts with special characters:

* Escape HTML entities or use plain-text representations.
* Avoid raw Unicode arrows or emojis; use Markdown alternatives.
* Always test the prompt standalone:

```bash
python script9.py "Pregunta con caracteres especiales: ¿Cómo hago que el robot siga la línea?"
```

* Check `history9.json` to verify proper saving and retrieval of characters.

---

### 21. Integrating RAG or External Documentation

RAG (Retrieval-Augmented Generation) allows the AI to reference external sources.

### A. Configuring Sources

* Identify which sources (PDFs, websites, images) should be used per category.
* For example, `script1.py` could reference official LEGO SPIKE Prime docs, while `script2.py` could reference WRO mechanical rules.
* Ensure that your AI prompt mentions to use external sources only when needed:

```text
- If unsure about an answer, reference the official documentation provided.
- Cite source URLs or sections explicitly.
```

### B. Implementing RAG

* Retrieve content from your external sources (PDFs, websites) in Python using libraries like `PyPDF2`, `requests`, or `BeautifulSoup`.
* Include the retrieved content in the `engineered_prompt` or append it dynamically before calling `client.responses.create()`.
* Keep token limits in mind; trim irrelevant parts.

### C. Testing RAG

* Test the integration by providing questions that require external info.
* Verify the AI cites the correct source.
* Monitor response length to ensure it does not exceed `max_output_tokens`.

---

### 22. Model Upgrades and Performance Considerations

You can swap the model in category scripts or `classify.py`.

### A. Upgrading the Model

* Example in `script9.py`:

```python
response = client.responses.create(
    model="gpt-5",
    input=final_input,
)
```

* Make sure your subscription or API key supports the upgraded model.

### B. Rate Limits and Costs

* OpenAI charges per token; monitor your usage especially if using `gpt-5`.
* Avoid excessively long prompts in production; keep `engineered_prompt` concise but complete.
* Implement logging to track API calls and token usage.

---

### 23. Security Considerations

* Never commit `.env` files with API keys.
* Use environment variables for all sensitive credentials.
* Consider adding a `.gitignore` entry for any local configuration containing secrets.

---
### 24. Github Workflow


---

### 25. Best Practices Recap

* Always test new categories standalone before integrating.
* Use structured examples in prompts.
* Handle special characters carefully.
* Log AI responses and history files for debugging.
* Keep prompts clear, concise, and category-specific.
* Regularly review external source integration and citations if using RAG.
* Monitor API usage, rate limits, and costs.

Following these guidelines ensures a robust, maintainable, and scalable FUNDESTEAM Chatbot backend.


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
