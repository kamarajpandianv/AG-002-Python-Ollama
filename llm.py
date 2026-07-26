from ollama import Client
from config import MODEL_NAME, OLLAMA_HOST
from logger import logger

client = Client(host=OLLAMA_HOST)


def generate_response(messages):
    """Send the conversation to the configured LLM and return the response."""

    try:
        answer = ""

        stream = client.chat(
            model=MODEL_NAME,
            messages=messages,
            stream=True
        )

        for chunk in stream:
            text = chunk["message"]["content"]
            print(text, end="", flush=True)
            answer += text

        return answer

    except Exception:
        logger.exception("LLM communication failed")
        return "Sorry, I couldn't communicate with the language model."