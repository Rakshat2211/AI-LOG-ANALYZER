import time
import ollama

from backend.core.config import settings


def generate_response(
    prompt: str,
) -> str:

    print(
        "[Performance] Sending request to Ollama..."
    )

    start = time.perf_counter()

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
            "num_predict":250,
            "top_p": 0.9,

        },

    )

    elapsed = (
        time.perf_counter() - start
    )

    print(
        f"[Performance] Ollama Response "
        f"received in {elapsed:.3f} sec"
    )

    return response["message"]["content"]