from llm.gemini_client import GeminiClient
from llm.prompts import DOC_SYSTEM_PROMPT
from graph.state import AgenticState


def documentation_agent(state: AgenticState) -> AgenticState:
    """
    Documentation Agent

    Responsibilities:
    - Generate professional project documentation
    - Explain architecture, setup, and usage
    - Produce README-style content
    """

    if not all([
        state.project_brief,
        state.product_spec,
        state.architecture_plan,
        state.backend_code,
        state.frontend_code
    ]):
        raise ValueError(
            "Missing required information. "
            "Core agents must complete before documentation."
        )

    client = GeminiClient(model_type="fast")

    prompt = f"""
Project Brief:
{state.project_brief}

Product Specification:
{state.product_spec}

Architecture Plan:
{state.architecture_plan}

Backend Overview:
{state.backend_code}

Frontend Overview:
{state.frontend_code}

QA Report:
{state.qa_report}

Code Review Report:
{state.code_review_report}

Generate professional documentation including:
1. Project overview
2. System architecture explanation
3. Tech stack
4. Setup instructions
5. How the system works (agent workflow)
6. How to run the app
7. Future improvements

Write it like a high-quality GitHub README.
"""

    documentation = client.generate(
        prompt=prompt,
        system_instruction=DOC_SYSTEM_PROMPT,
        temperature=0.25
    )

    state.documentation = documentation
    state.final_summary = documentation  # final output for UI

    return state
