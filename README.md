# 🤖 RuleBot — Rule-Based AI Chatbot

**DecodeLabs Internship | Artificial Intelligence | Project 01**

---

## 📌 Project Overview

RuleBot is a beginner-friendly, rule-based AI chatbot built entirely in Python.  
It uses `if-elif-else` conditions to match user input and return predefined responses.  
No machine learning, no APIs, no paid services — just pure Python logic.

This project demonstrates:
- Basic Python programming (functions, loops, conditionals)
- String manipulation and input cleaning
- Structuring a simple conversational AI using rules
- Writing clean, well-commented, readable code

---

## 🎯 Objective

Build a simple chatbot that responds to predefined user inputs using Python if-else logic, runs in the terminal, and is easy enough for a complete beginner to understand.

---

## 🗂️ Project Structure

```
Project 01/
│
├── chatbot.py        # Main chatbot script — all the logic lives here
├── README.md         # Project documentation (this file)
└── requirements.txt  # Dependency information
```

---

## ⚙️ Requirements

### Python Version
- Python **3.6 or higher** (developed and tested on Python 3.x)

### External Libraries
**None.** This project uses only Python's built-in standard library:
- `datetime` — used to display the current time and date (already included with Python)

No `pip install` commands are needed.

---

## 🚀 Installation & Setup

### Step 1 — Check Python is installed
Open your terminal (Command Prompt, PowerShell, or Terminal) and run:

```bash
python --version
```

You should see something like `Python 3.10.x`. If Python is not installed, download it from [python.org](https://www.python.org/downloads/).

### Step 2 — Download or clone the project

**Option A — Download ZIP:**
1. Download the project folder.
2. Extract it to a location of your choice.

**Option B — Clone via Git:**
```bash
git clone https://github.com/your-username/rule-based-ai-chatbot.git
cd rule-based-ai-chatbot
```

### Step 3 — Navigate to the project folder
```bash
cd "path/to/Project 01"
```

---

## ▶️ How to Run

```bash
python chatbot.py
```

That's it! The chatbot will start immediately in your terminal.

---

## 💬 Sample Input / Output

```
=======================================================
        Welcome to RuleBot 🤖
        DecodeLabs Internship — Project 01
=======================================================
  I am a simple rule-based AI chatbot.
  I respond to common questions and greetings.

  Try asking me:
    • Hello / Hi / Hey
    • How are you?
    • What is your name?
    • What can you do?
    • What is AI?
    • Thank you

  Type  'bye', 'exit', or 'quit'  to stop.
=======================================================

You: hello
RuleBot: Hello! 👋 Great to see you! How can I help you today?

You: What is your name?
RuleBot: I'm RuleBot 🤖 — a simple rule-based AI chatbot built with Python!

You: what is ai
RuleBot: AI stands for Artificial Intelligence. 🧠
         It is the simulation of human intelligence by computer systems.
         AI can learn, reason, problem-solve, and understand language.
         Examples include chatbots, voice assistants, and image recognition.

You: how are you?
RuleBot: I'm doing great, thanks for asking! 😊 I'm always ready to chat.

You: what can you do?
RuleBot: Here's what I can help you with:
           • Answer basic questions about myself
           • Tell you what AI is
           • Have a friendly conversation
           • Respond to greetings and farewells
         Just type your question and I'll do my best! 😊

You: thank you
RuleBot: You're very welcome! 😊 Feel free to ask me anything else.

You: what time is it?
RuleBot: The current time on your system is 10:45 AM ⏰

You: who made you?
RuleBot: I was built as part of DecodeLabs Internship - Project 01! 🚀
         I'm a rule-based chatbot written entirely in Python.

You: randomstuff
RuleBot: Hmm, I'm not sure how to answer that. 🤔
         Try asking me things like:
           → 'What is your name?'
           → 'What is AI?'
           → 'What can you do?'
         Type 'help' to see all my capabilities!

You: bye
RuleBot: Goodbye! 👋 Thanks for chatting. Have a great day!
=======================================================
```

---

## 🧪 How to Test the Chatbot

Try each of the following inputs to verify all features work:

| Test Input         | Expected Behaviour                          |
|--------------------|---------------------------------------------|
| `hello`            | Greeting response                           |
| `Hi`               | Greeting response (case-insensitive)        |
| `HEY`              | Greeting response (case-insensitive)        |
| `how are you?`     | Well-being response                         |
| `what is your name?` | Returns chatbot name                      |
| `what can you do?` | Lists capabilities                          |
| `what is AI?`      | Explains Artificial Intelligence            |
| `thank you`        | Polite acknowledgement                      |
| `who made you?`    | Returns creator/project info                |
| `what time is it?` | Shows current system time                   |
| `   HELLO   `      | Trims spaces, responds correctly            |
| `xyz123`           | Fallback / unknown input response           |
| *(blank Enter)*    | Prompts user to type something              |
| `bye`              | Exits the chatbot gracefully                |
| `exit`             | Exits the chatbot gracefully                |
| `quit`             | Exits the chatbot gracefully                |

---

## 🔍 How It Works (Beginner Explanation)

1. **`display_welcome()`** — Prints a banner with instructions when the chatbot starts.
2. **`get_response(user_input)`** — Cleans the input (lowercase + strip spaces), then checks it against a series of `if-elif-else` rules and returns a matching response.
3. **`main()`** — Runs a `while True` loop that keeps asking for input. If the user types `bye`, `exit`, or `quit`, the loop breaks and the program ends.

```
User types input
       ↓
Input is cleaned (lowercase + strip)
       ↓
Checked against if-elif-else rules
       ↓
Matching response is printed
       ↓
Loop repeats (until bye/exit/quit)
```

---

## 📁 Suggested GitHub Repository Name

```
rule-based-ai-chatbot
```

### Steps to Upload to GitHub

1. **Create a new repository** on [github.com](https://github.com):
   - Repository name: `rule-based-ai-chatbot`
   - Description: `A beginner-friendly rule-based AI chatbot built with Python — DecodeLabs Internship Project 01`
   - Visibility: Public
   - Do **not** initialize with README (you already have one)

2. **Initialize Git locally** (inside the project folder):
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Rule-Based AI Chatbot - DecodeLabs Project 01"
   ```

3. **Connect and push to GitHub:**
   ```bash
   git remote add origin https://github.com/your-username/rule-based-ai-chatbot.git
   git branch -M main
   git push -u origin main
   ```

4. **Verify** — Visit your repository URL to confirm all files are uploaded.

---

## ✅ Project Requirements Checklist

- [x] Uses Python as the programming language
- [x] Handles greetings: `hello`, `hi`, `hey`
- [x] Responds to `How are you?`
- [x] Responds to `What is your name?`
- [x] Responds to `What can you do?`
- [x] Responds to `What is AI?`
- [x] Responds to `Thank you`
- [x] Uses `if-elif-else` conditions for all responses
- [x] Runs continuously using a `while` loop
- [x] Exits on `bye`, `exit`, or `quit`
- [x] Displays a friendly welcome message with clear instructions
- [x] Handles unknown inputs with a polite fallback response
- [x] Case-insensitive input handling
- [x] Strips unnecessary spaces from input
- [x] Code is commented for beginners
- [x] No machine learning, LLM APIs, or paid services used
- [x] No external libraries required

---

## 👤 Author

Built for **DecodeLabs Artificial Intelligence Internship**  
Project 01 — Rule-Based AI Chatbot

---

## 📄 License

This project is open-source and free to use for educational purposes.
