from llm.gemini_client import GeminiClient
from llm.prompts import CEO_SYSTEM_PROMPT
from graph.state import AgenticState

def ceo_agent(state: AgenticState) -> AgenticState:
    """
    CEO / Orchestrator Agent

    Responsibilities:
    - Understand user input
    - Convert it into a structured project brief
    - Update global state
    """

    client = GeminiClient(model_type="fast")

    prompt = f"""
User idea:
{state.user_input}

Create a structured project brief with:
- Problem statement
- Goals
- Constraints
- Success criteria
"""

    project_brief = client.generate(
        prompt=prompt,
        system_instruction=CEO_SYSTEM_PROMPT,
        temperature=0.2    
    )

    #Update state
    state.project_brief = project_brief

    return state