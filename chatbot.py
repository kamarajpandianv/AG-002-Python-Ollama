from llm import generate_response
from config import PROMPT_FILE
from router import route_command
from logger import logger

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

    logger.info("Angel started")

    while True:

        prompt = input("You: ")
        logger.info(f"User: {prompt}")

        if prompt.lower() == "exit":
            logger.info("Angel closed")
            break

        handled, response = route_command(prompt)

        if handled:
            logger.info(f"Tool executed: {prompt}")
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

        logger.info(f"LLM response generated ({len(answer)} characters)")

        print()

        messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )