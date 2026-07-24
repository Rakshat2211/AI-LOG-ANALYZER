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

    prompt = build_prompt(
        analysis_context
    )

    return generate_response(
        prompt
    )