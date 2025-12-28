from llm.gemini_client import GeminiClient
from llm.prompts import FRONTEND_DEV_SYSTEM_PROMPT
from graph.state import AgenticState

def frontend_dev_agent(state: AgenticState) -> AgenticState:
    """
    Frontend Developer Agent

    Responsibilities:
    - Design Streamlit UI
    - Define layout and navigation
    - Connect UI to backend APIs conceptually
    """

    if not state.product_spec or not state.backend_code:
        raise ValueError(
            "Product spec or backend code missing. "
            "PM and Backend Dev agents must run first."
        )
    
    client = GeminiClient(model_type="fast")

    prompt = f"""
Product Requirements:
{state.product_spec}

Backend Design & APIs:
{state.backend_code}

Design the Streamlit frontend:

1. Page structure and navigation
2. User inputs and forms
3. How frontend interacts with backend APIs
4. Provide Streamlit code skeleton (app.py style)

Rules:
- Focus on clarity and usability
- Do NOT implement full backend calls
- Keep code modular and readable
"""
    
    frontend_code = client.generate(
        prompt=prompt,
        system_instruction=FRONTEND_DEV_SYSTEM_PROMPT,
        temperature=0.3
    )

    state.frontend_code =  frontend_code

    return state