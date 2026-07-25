from ollama import chat
from config import MODEL_NAME


def generate_response(messages):
    """
    Send the conversation to the configured LLM and
    return the assistant's response.
    """

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