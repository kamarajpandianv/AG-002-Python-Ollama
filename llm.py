from ollama import chat
from config import MODEL_NAME
from logger import logger


def generate_response(messages):
    """Send the conversation to the configured LLM and return the response."""

    try:
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

        return answer

    except Exception as e:
        logger.exception("LLM communication failed")
        return "Sorry, I couldn't communicate with the language model."