from datetime import datetime
from pathlib import Path
import json

from config import NOTES_FILE, REMINDERS_FILE


# ---------- Time Tool ----------

def get_current_time():
    """Return the current local time."""
    return datetime.now().strftime("%I:%M:%S %p")


# ---------- Calculator Tool ----------

def calculate(expression):
    """Evaluate a mathematical expression."""
    try:
        return eval(expression)
    except Exception:
        return "Sorry, I couldn't calculate that."


# ---------- Notes Tool ----------

def save_note(note):
    with open(NOTES_FILE, "a", encoding="utf-8") as file:
        file.write(note + "\n")

    return "Note saved."


def show_notes():
    try:
        with open(NOTES_FILE, "r", encoding="utf-8") as file:
            notes = file.readlines()

        if not notes:
            return "No notes found."

        output = ""

        for i, note in enumerate(notes, start=1):
            output += f"{i}. {note}"

        return output

    except FileNotFoundError:
        return "No notes found."


# ---------- Reminder Tool ----------

def save_reminder(task):

    reminder = {
        "task": task
    }

    if REMINDERS_FILE.exists():

        with open(REMINDERS_FILE, "r", encoding="utf-8") as file:
            reminders = json.load(file)

    else:
        reminders = []

    reminders.append(reminder)

    with open(REMINDERS_FILE, "w", encoding="utf-8") as file:
        json.dump(reminders, file, indent=4)

    return "Reminder saved."


def show_reminders():

    if not REMINDERS_FILE.exists():
        return "No reminders found."

    with open(REMINDERS_FILE, "r", encoding="utf-8") as file:
        reminders = json.load(file)

    if not reminders:
        return "No reminders found."

    output = ""

    for i, reminder in enumerate(reminders, start=1):
        output += f"{i}. {reminder['task']}\n"

    return output