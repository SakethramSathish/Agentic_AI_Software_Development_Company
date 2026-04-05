"""
Streaming wrapper for the LangGraph pipeline.
Yields real-time events as each agent node completes.
"""

from graph.graph_builder import build_graph
from graph.state import AgenticState
from utils.validators import validate_initial_state
from utils.logger import setup_logger

logger = setup_logger(__name__)

# Map node names to their primary output field in AgenticState
NODE_OUTPUT_FIELDS = {
    "ceo": "project_brief",
    "product_manager": "product_spec",
    "system_architect": "architecture_plan",
    "cto": "cto_decision",
    "backend_dev": "backend_code",
    "frontend_dev": "frontend_code",
    "ai_engineer": "ai_design_notes",
    "qa": "qa_report",
    "code_reviewer": "code_review_report",
    "documentation": "final_summary",
}

AGENT_LABELS = {
    "ceo": "CEO",
    "product_manager": "Product Manager",
    "system_architect": "System Architect",
    "cto": "CTO",
    "backend_dev": "Backend Developer",
    "frontend_dev": "Frontend Developer",
    "ai_engineer": "AI Engineer",
    "qa": "QA Engineer",
    "code_reviewer": "Code Reviewer",
    "documentation": "Documentation Writer",
}

AGENT_EMOJIS = {
    "ceo": "\U0001f9e0",
    "product_manager": "\U0001f4e6",
    "system_architect": "\U0001f3d7\ufe0f",
    "cto": "\U0001f454",
    "backend_dev": "\U0001f4bb",
    "frontend_dev": "\U0001f3a8",
    "ai_engineer": "\U0001f916",
    "qa": "\U0001f9ea",
    "code_reviewer": "\U0001f9fe",
    "documentation": "\U0001f4da",
}


def stream_graph(user_idea: str):
    """
    Generator that yields events as each LangGraph node completes.

    Yields dicts with:
        agent   – node key name
        label   – human-readable name
        emoji   – agent emoji
        status  – "done"
        field   – AgenticState field name
        output  – the agent's output text
    """
    initial_state = AgenticState(user_input=user_idea)
    validate_initial_state(initial_state)

    compiled_app = build_graph()
    logger.info("Starting streaming graph execution")

    for event in compiled_app.stream(initial_state.model_dump()):
        for node_name, state_update in event.items():
            # Skip internal LangGraph events
            if node_name.startswith("__"):
                continue

            output_field = NODE_OUTPUT_FIELDS.get(node_name)
            output_value = ""

            if output_field and isinstance(state_update, dict):
                output_value = state_update.get(output_field, "")

            yield {
                "agent": node_name,
                "label": AGENT_LABELS.get(node_name, node_name),
                "emoji": AGENT_EMOJIS.get(node_name, "\U0001f527"),
                "status": "done",
                "field": output_field or "",
                "output": str(output_value) if output_value else "",
            }

            logger.info(f"Agent '{node_name}' completed")

    logger.info("Streaming graph execution completed")
