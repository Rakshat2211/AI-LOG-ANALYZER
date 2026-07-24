import ollama

from backend.core.config import settings


def generate_response(
    prompt: str,
) -> str:

    response = ollama.chat(

        model=settings.OLLAMA_MODEL,

        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],

        options={
            "temperature": settings.OLLAMA_TEMPERATURE,
        },
    )

    return response["message"]["content"]