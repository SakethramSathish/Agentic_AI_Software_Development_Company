from llm.gemini_client import GeminiClient
from llm.prompts import BACKEND_DEV_SYSTEM_PROMPT
from graph.state import AgenticState

def backend_dev_agent(state: AgenticState) -> AgenticState:
    """
    Backend Developer Agent

    Responsibilities:
    - Design backend logic
    - Define APIs
    - Suggest database schema
    - Generate clean Python backend code (FastAPI-style)
    """

    if not state.architecture_plan:
        raise ValueError(
            "Architecture plan missing. System Architect + CTO must run first."
        )
    
    client = GeminiClient(model_type="fast")

    prompt = f"""
Approved Architecture:
{state.architecture_plan}

Based on this architecture:

1. Design backend responsibilities
2. Define REST API endpoints (with methods)
3. Propose database schema
4. Generate a clean Python backend skeleton (FastAPI style)

Rules:
- Focus on structure, not full implementation
- Keep code modular and readable
"""
    
    backend_code = client.generate(
        prompt=prompt,
        system_instruction=BACKEND_DEV_SYSTEM_PROMPT,
        temperature=0.3
    )

    state.backend_code = backend_code

    return state