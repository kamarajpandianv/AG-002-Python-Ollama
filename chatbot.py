from ollama import chat
from config import MODEL_NAME, PROMPT_FILE
from router import route_command

with open(PROMPT_FILE, "r", encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read()


def run_chat():

    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    print("Angel v1.0")
    print("Local AI Assistant")
    print("Type 'exit' to quit.\n")

    while True:

        prompt = input("You: ")

        if prompt.lower() == "exit":
            break

        handled, response = route_command(prompt)

        if handled:
            print("\nAngel:", response)
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





