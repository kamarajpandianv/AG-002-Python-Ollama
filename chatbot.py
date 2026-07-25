from ollama import chat
from config import MODEL_NAME, SYSTEM_PROMPT
from tools import (
    get_current_time,
    calculate,
    save_note,
    show_notes,
    save_reminder,
    show_reminders
)



def run_chat():

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    print("Angel v0.4")
    print("Type 'exit' to quit.\n")

    while True:

        prompt = input("You: ")

        if prompt.lower() == "exit":
            break

        # ---------- Time Tool ----------
        if "time" in prompt.lower():

            print("\nAngel:", get_current_time())
            print()

            continue

        # ---------- Calculator Tool ----------

        if prompt.lower().startswith("calculate"):

            expression = prompt[9:].strip()

            print("\nAngel:", calculate(expression))
            print()

            continue

        # ---------- Notes Tool ----------

        if prompt.lower().startswith("note"):

            note = prompt[4:].strip()

            print("\nAngel:", save_note(note))
            print()

            continue


        if prompt.lower() == "show notes":

            print("\nAngel:")
            print(show_notes())
            print()

            continue        

        # ---------- Reminder Tool ----------
        # ---------- Reminder Tool ----------

        if prompt.lower().startswith("remind me to"):

            task = prompt[13:].strip()

            print("\nAngel:", save_reminder(task))
            print()

            continue

        elif prompt.lower().startswith("remind"):

            task = prompt[6:].strip()

            print("\nAngel:", save_reminder(task))
            print()

            continue

        # ---------- Show Reminders ----------

        if prompt.lower() in ["show reminders", "show reminder"]:

            print("\nAngel:")
            print(show_reminders())
            print()

            continue           

        # ---------- Normal Chat ----------
        messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        print("\nAngel: ", end="", flush=True)

        answer = ""

        stream = chat(
            model=MODEL_NAME,
            messages=messages,
            stream=True
        )

        for chunk in stream:
            text = chunk["message"]["content"]
            print(text, end="", flush=True)
            answer += text

        print()

        messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )





