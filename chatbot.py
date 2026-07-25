from ollama import chat
from config import MODEL_NAME, SYSTEM_PROMPT
from tools import get_current_time


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