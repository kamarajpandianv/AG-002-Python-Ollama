"""
config.py

Central configuration for Angel AI Assistant.
"""

from pathlib import Path
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ---------------------------------------------------------------------
# Base Directories
# ---------------------------------------------------------------------

BASE_DIR = Path(__file__).parent

DATA_DIR = BASE_DIR / "data"
PROMPTS_DIR = BASE_DIR / "prompts"
LOGS_DIR = BASE_DIR / "logs"

# Create required directories
DATA_DIR.mkdir(exist_ok=True)
PROMPTS_DIR.mkdir(exist_ok=True)
LOGS_DIR.mkdir(exist_ok=True)

# ---------------------------------------------------------------------
# Application
# ---------------------------------------------------------------------

APP_NAME = os.getenv("APP_NAME", "Angel")
VERSION = os.getenv("VERSION", "1.1.0")

# ---------------------------------------------------------------------
# LLM
# ---------------------------------------------------------------------

MODEL_NAME = os.getenv("MODEL_NAME", "qwen3:8b")
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://localhost:11434")

# ---------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
DEBUG = os.getenv("DEBUG", "False").lower() == "true"

# ---------------------------------------------------------------------
# Data Files
# ---------------------------------------------------------------------

NOTES_FILE = DATA_DIR / "notes.txt"
REMINDERS_FILE = DATA_DIR / "reminders.json"

# ---------------------------------------------------------------------
# Prompt
# ---------------------------------------------------------------------

PROMPT_FILE = PROMPTS_DIR / "system_prompt.txt"