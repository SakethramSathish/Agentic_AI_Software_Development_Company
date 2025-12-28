from llm.gemini_client import GeminiClient
from llm.prompts import AI_ENGINEER_SYSTEM_PROMPT
from graph.state import AgenticState


def ai_engineer_agent(state: AgenticState) -> AgenticState:
    """
    AI / LLM Engineer Agent

    Responsibilities:
    - Review Gemini usage across agents
    - Suggest prompt improvements
    - Design memory & context handling strategy
    - Suggest cost and performance optimizations
    """

    if not state.architecture_plan:
        raise ValueError(
            "Architecture plan missing. Architect + CTO must run first."
        )

    client = GeminiClient(model_type="fast")

    prompt = f"""
System Architecture:
{state.architecture_plan}

Current Agent Outputs:
- Backend Code: {bool(state.backend_code)}
- Frontend Code: {bool(state.frontend_code)}

Analyze the AI usage and provide:
1. Prompt optimization suggestions
2. Context window management strategy
3. Memory design (short-term vs long-term)
4. Cost optimization tips for Gemini
5. Failure handling & retry strategy
"""

    ai_design_notes = client.generate(
        prompt=prompt,
        system_instruction=AI_ENGINEER_SYSTEM_PROMPT,
        temperature=0.25
    )

    state.ai_design_notes = ai_design_notes

    return state
