from datetime import datetime


def get_current_time():
    """Return the current local time."""
    return datetime.now().strftime("%I:%M:%S %p")


def calculate(expression):
    """Evaluate a mathematical expression."""
    try:
        return eval(expression)
    except Exception:
        return "Sorry, I couldn't calculate that."


def save_note(note):
    with open("notes.txt", "a", encoding="utf-8") as file:
        file.write(note + "\n")
    return "Note saved."


def show_notes():
    try:
        with open("notes.txt", "r", encoding="utf-8") as file:
            notes = file.readlines()

        if not notes:
            return "No notes found."

        output = ""

        for i, note in enumerate(notes, start=1):
            output += f"{i}. {note}"

        return output

    except FileNotFoundError:
        return "No notes found."