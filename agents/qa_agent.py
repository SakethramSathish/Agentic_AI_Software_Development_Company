from llm.gemini_client import GeminiClient
from llm.prompts import QA_SYSTEM_PROMPT
from graph.state import AgenticState


def qa_agent(state: AgenticState) -> AgenticState:
    """
    QA Engineer Agent

    Responsibilities:
    - Verify outputs against product requirements
    - Identify missing features or logical gaps
    - Flag inconsistencies between frontend, backend, and architecture
    """

    if not state.product_spec:
        raise ValueError("Product specification missing. PM agent must run first.")

    client = GeminiClient(model_type="fast")

    prompt = f"""
Product Requirements:
{state.product_spec}

Architecture Plan:
{state.architecture_plan}

Backend Output:
{state.backend_code}

Frontend Output:
{state.frontend_code}

AI Design Notes:
{state.ai_design_notes}

Perform QA review and provide:
1. Missing features
2. Logical inconsistencies
3. Integration issues
4. Risk areas
5. Clear recommendations

Do NOT rewrite code.
Do NOT suggest new features outside scope.
"""

    qa_report = client.generate(
        prompt=prompt,
        system_instruction=QA_SYSTEM_PROMPT,
        temperature=0.2
    )

    state.qa_report = qa_report

    return state
