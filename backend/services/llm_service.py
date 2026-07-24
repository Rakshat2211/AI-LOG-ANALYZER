from backend.services.ollama_service import (
    generate_response,
)


def generate_ai_analysis(
    analysis_context: str,
) -> str:
    """
    Generates an AI-powered analysis
    using the configured LLM provider.
    """

    return generate_response(
        analysis_context
    )