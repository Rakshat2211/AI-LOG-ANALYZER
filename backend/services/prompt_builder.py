def build_prompt(
    analysis_context: str,
) -> str:
    """
    Builds the prompt that will be sent
    to the Large Language Model.
    """

    system_prompt = """
You are an experienced Site Reliability Engineer.

You are analysing production application logs.

Use only the supplied log analysis report.

Do not invent information.

If information is missing, clearly state that.

Provide a concise report.

Limit the total response to approximately 150 words.

Use the following format:

1. Executive Summary
2. Root Cause
3. Severity
4. Recommendations

Do not repeat the supplied statistics.
"""

    return f"""

{system_prompt}

Log Analysis Report

------------------------

{analysis_context}

"""