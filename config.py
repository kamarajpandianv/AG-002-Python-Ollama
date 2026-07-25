from pathlib import Path

# Project Root Directory
BASE_DIR = Path(__file__).parent

# Model Configuration
MODEL_NAME = "qwen3:8b"

# Folder Paths
DATA_DIR = BASE_DIR / "data"
PROMPTS_DIR = BASE_DIR / "prompts"
LOGS_DIR = BASE_DIR / "logs"
INTEGRATIONS_DIR = BASE_DIR / "integrations"
TESTS_DIR = BASE_DIR / "tests"

# Data Files
NOTES_FILE = DATA_DIR / "notes.txt"
REMINDERS_FILE = DATA_DIR / "reminders.json"

# Prompt Files
PROMPT_FILE = PROMPTS_DIR / "system_prompt.txt"