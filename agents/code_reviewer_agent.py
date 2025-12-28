from llm.gemini_client import GeminiClient
from llm.prompts import CODE_REVIEWER_SYSTEM_PROMPT
from graph.state import AgenticState


def code_reviewer_agent(state: AgenticState) -> AgenticState:
    """
    Code Reviewer Agent

    Responsibilities:
    - Review backend and frontend code quality
    - Detect bugs, anti-patterns, and inefficiencies
    - Suggest improvements and refactoring ideas
    """

    if not state.backend_code or not state.frontend_code:
        raise ValueError(
            "Backend or frontend code missing. "
            "Development agents must run first."
        )

    client = GeminiClient(model_type="fast")

    prompt = f"""
Backend Code:
{state.backend_code}

Frontend Code:
{state.frontend_code}

Perform a senior-level code review and provide:
1. Code quality issues
2. Potential bugs or edge cases
3. Style and readability feedback
4. Suggested refactors
5. Best practice violations (if any)

Do NOT rewrite the entire code.
Do NOT introduce new features.
"""

    code_review_report = client.generate(
        prompt=prompt,
        system_instruction=CODE_REVIEWER_SYSTEM_PROMPT,
        temperature=0.2
    )

    state.code_review_report = code_review_report

    return state
