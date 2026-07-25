"""
config.py

Central configuration for the Angel AI Assistant.
"""

from pathlib import Path

# ---------------------------------------------------------------------
# Base Directories
# ---------------------------------------------------------------------

BASE_DIR = Path(__file__).parent

DATA_DIR = BASE_DIR / "data"
PROMPTS_DIR = BASE_DIR / "prompts"
LOGS_DIR = BASE_DIR / "logs"

# ---------------------------------------------------------------------
# LLM Configuration
# ---------------------------------------------------------------------

MODEL_NAME = "qwen3:8b"

# ---------------------------------------------------------------------
# Data Files
# ---------------------------------------------------------------------

NOTES_FILE = DATA_DIR / "notes.txt"
REMINDERS_FILE = DATA_DIR / "reminders.json"

# ---------------------------------------------------------------------
# Prompt Files
# ---------------------------------------------------------------------

PROMPT_FILE = PROMPTS_DIR / "system_prompt.txt"