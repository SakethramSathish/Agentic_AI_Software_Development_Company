from llm.gemini_client import GeminiClient
from llm.prompts import PM_SYSTEM_PROMPT
from graph.state import AgenticState

def product_manager_agent(state: AgenticState) -> AgenticState:
    """
    Product Manager Agent

    Responsibilities:
    - Convert project brief into product requirements
    - Define features, user stories, and MVP scope
    """

    if not state.project_brief:
        raise ValueError("Project brief missing. CEO agent must run first.")
    
    client = GeminiClient(model_type="fast")

    prompt = f"""
Project Brief:
{state.project_brief}

Convert this into:
1. Feature list
2. User stories
3. MVP scope
4. Acceptance criteria
"""
    
    product_spec = client.generate(
        prompt=prompt,
        system_instruction=PM_SYSTEM_PROMPT,
        temperature=0.3
    )

    state.product_spec = product_spec

    return state