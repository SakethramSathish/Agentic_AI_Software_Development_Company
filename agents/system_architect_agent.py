from llm.gemini_client import GeminiClient
from llm.prompts import ARCHITECT_SYSTEM_PROMPT
from graph.state import AgenticState

def system_architect_agent(state: AgenticState) -> AgenticState:
    """
    System Architect Agent

    Responsibilities:
    - Design system architecture
    - Define frontend, backend, database, and AI components
    - Outline data flow and APIs
    """

    if not state.product_spec:
        raise ValueError(
            "Product specification missing. Product Manager agent must run first."
        )
    
    client = GeminiClient(model_type="fast")

    prompt = f"""
Product Specification:
{state.product_spec}

Design the system architecture including:
- High-level architecture diagram (described in text)
- Frontend responsibilities
- Backend responsibilities
- Database design
- AI/LLM components
- API boundaries
"""
    
    architecture_plan = client.generate(
        prompt=prompt,
        system_instruction=ARCHITECT_SYSTEM_PROMPT,
        temperature=0.25
    )

    state.architecture_plan = architecture_plan

    return state