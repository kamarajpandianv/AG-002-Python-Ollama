from llm import generate_response
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

        answer = generate_response(messages)

        print()

        messages.append(
            {
                "role": "assistant",
                "content": answer
            }   
        )