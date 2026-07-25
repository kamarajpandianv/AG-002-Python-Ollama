# Angel 🤖

Angel is a modular local AI assistant built with Python and Ollama.

It is designed as a learning project to explore modern AI application development while following professional software engineering practices.

## Features

- 💬 Local AI chat using Ollama
- 🧠 Conversation history
- 🕒 Time tool
- 🧮 Calculator
- 📝 Notes
- ⏰ Reminders
- 🔀 Command Router
- 🤖 Dedicated LLM Service
- ⚙️ Configurable prompts

---

## Project Structure

```text
AG-002_Python_Ollama/
│
├── main.py
├── chatbot.py
├── router.py
├── llm.py
├── tools.py
├── config.py
│
├── data/
├── prompts/
├── integrations/
├── logs/
├── tests/
└── docs/
```

---

## Requirements

- Python 3.11+
- Ollama
- Qwen3:8B (or another supported model)

---

## Run

```bash
python main.py
```