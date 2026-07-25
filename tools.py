"""
tools.py

Built-in tools for the Angel AI Assistant.
"""

from datetime import datetime
import json

from config import NOTES_FILE, REMINDERS_FILE


# ---------------------------------------------------------------------
# Time Tool
# ---------------------------------------------------------------------

def get_current_time() -> str:
    """Return the current system time."""
    return datetime.now().strftime("%I:%M:%S %p")


# ---------------------------------------------------------------------
# Calculator Tool
# ---------------------------------------------------------------------

def calculate(expression: str) -> str:
    """Evaluate a mathematical expression."""

    expression = expression.strip()

    if not expression:
        return "Please provide an expression."

    try:
        result = eval(expression)
        return str(result)

    except Exception:
        return "Invalid mathematical expression."


# ---------------------------------------------------------------------
# Notes Tool
# ---------------------------------------------------------------------

def save_note(note: str) -> str:
    """Save a note."""

    note = note.strip()

    if not note:
        return "Please enter a note."

    with open(NOTES_FILE, "a", encoding="utf-8") as file:
        file.write(note + "\n")

    return "Note saved."


def show_notes() -> str:
    """Display all saved notes."""

    try:
        with open(NOTES_FILE, "r", encoding="utf-8") as file:
            notes = [line.strip() for line in file if line.strip()]

        if not notes:
            return "No notes found."

        return "\n".join(
            f"{index}. {note}"
            for index, note in enumerate(notes, start=1)
        )

    except FileNotFoundError:
        return "No notes found."


# ---------------------------------------------------------------------
# Reminder Tool
# ---------------------------------------------------------------------

def save_reminder(task: str) -> str:
    """Save a reminder."""

    task = task.strip()

    if not task:
        return "Please enter a reminder."

    try:
        with open(REMINDERS_FILE, "r", encoding="utf-8") as file:
            reminders = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        reminders = []

    reminders.append(task)

    with open(REMINDERS_FILE, "w", encoding="utf-8") as file:
        json.dump(reminders, file, indent=4)

    return "Reminder saved."


def show_reminders() -> str:
    """Display all reminders."""

    try:
        with open(REMINDERS_FILE, "r", encoding="utf-8") as file:
            reminders = json.load(file)

        if not reminders:
            return "No reminders found."

        return "\n".join(
            f"{index}. {reminder}"
            for index, reminder in enumerate(reminders, start=1)
        )

    except (FileNotFoundError, json.JSONDecodeError):
        return "No reminders found."