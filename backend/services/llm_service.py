import time

from backend.services.prompt_builder import (
    build_prompt,
)

from backend.services.ollama_service import (
    generate_response,
)


def generate_ai_analysis(
    analysis_context: str,
) -> str:
    """
    Generates AI analysis
    from structured log context.
    """

    total_start = time.perf_counter()

    # -------------------------
    # Prompt Builder
    # -------------------------

    prompt_start = time.perf_counter()

    prompt = build_prompt(
        analysis_context
    )

    prompt_time = (
        time.perf_counter() - prompt_start
    )

    print(
        f"[Performance] Prompt Builder : "
        f"{prompt_time:.3f} sec"
    )

    # -------------------------
    # Ollama
    # -------------------------

    llm_start = time.perf_counter()

    response = generate_response(
        prompt
    )

    llm_time = (
        time.perf_counter() - llm_start
    )

    print(
        f"[Performance] Ollama         : "
        f"{llm_time:.3f} sec"
    )

    total_time = (
        time.perf_counter() - total_start
    )

    print(
        f"[Performance] Total AI       : "
        f"{total_time:.3f} sec"
    )

    return response