from tools import (
    get_current_time,
    calculate,
    save_note,
    show_notes,
    save_reminder,
    show_reminders
)


def route_command(prompt: str):
    """
    Routes user commands to the appropriate tool.

    Returns:
        (handled, response)

        handled = True  -> Tool executed.
        handled = False -> Send prompt to LLM.
    """

    command = prompt.lower().strip()

    # ---------- Time ----------

    if "time" in command:
        return True, get_current_time()

    # ---------- Calculator ----------

    if command.startswith("calculate"):

        expression = prompt[len("calculate"):].strip()
        return True, calculate(expression)

    # ---------- Notes ----------

    if command.startswith("note"):

        note = prompt[len("note"):].strip()
        return True, save_note(note)

    if command == "show notes":
        return True, show_notes()

    # ---------- Reminders ----------

    if command.startswith("remind me to"):

        task = prompt[len("remind me to"):].strip()
        return True, save_reminder(task)

    if command.startswith("remind"):

        task = prompt[len("remind"):].strip()
        return True, save_reminder(task)

    if command in ["show reminders", "show reminder"]:
        return True, show_reminders()

    # ---------- Not a Tool ----------

    return False, None