from backend.services.prompt_builder import build_prompt


def test_prompt_contains_system_prompt():

    prompt = build_prompt("Sample Context")

    assert "Site Reliability Engineer" in prompt

    assert "Executive Summary" in prompt

    assert "Root Cause" in prompt

    assert "Severity" in prompt

    assert "Recommendations" in prompt


def test_prompt_contains_context():

    context = "This is a test report."

    prompt = build_prompt(context)

    assert context in prompt


def test_prompt_contains_heading():

    prompt = build_prompt("ABC")

    assert "Log Analysis Report" in prompt