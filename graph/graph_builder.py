"""
LangGraph builder for the Agentic AI Software Company.

This file:
- Assembles the full agent graph
- Defines execution order
- Applies conditional routing
"""

from langgraph.graph import StateGraph, END

from graph.state import AgenticState
from graph.nodes import (
    ceo_node,
    product_manager_node,
    system_architect_node,
    cto_node,
    backend_dev_node,
    frontend_dev_node,
    ai_engineer_node,
    qa_node,
    code_reviewer_node,
    documentation_node,
)
from graph.edges import (
    route_after_cto,
    route_after_code_review,
)
from utils.validators import validate_initial_state
from utils.logger import setup_logger

logger = setup_logger(__name__)

def build_graph():
    """
    Build and return the compiled LangGraph application.
    """
    logger.info("Building Agentic AI Software Company graph")

    graph = StateGraph(AgenticState)

    #Add Nodes

    graph.add_node("ceo", ceo_node)
    graph.add_node("product_manager", product_manager_node)
    graph.add_node("system_architect", system_architect_node)
    graph.add_node("cto", cto_node)

    graph.add_node("backend_dev", backend_dev_node)
    graph.add_node("frontend_dev", frontend_dev_node)
    graph.add_node("ai_engineer", ai_engineer_node)

    graph.add_node("qa", qa_node)
    graph.add_node("code_reviewer", code_reviewer_node)

    graph.add_node("documentation", documentation_node)

    #Entry Point

    graph.set_entry_point("ceo")

    #Linear Executive Flow

    graph.add_edge("ceo", "product_manager")
    graph.add_edge("product_manager", "system_architect")
    graph.add_edge("system_architect", "cto")

    #CTO Conditional Routing

    graph.add_conditional_edges(
        "cto",
        route_after_cto,
        {
            "backend_dev": "backend_dev",
            "system_architect": "system_architect",
        },
    )

    #Development Flow

    graph.add_edge("backend_dev", "frontend_dev")
    graph.add_edge("frontend_dev", "ai_engineer")

    #Quality Control Flow

    graph.add_edge("ai_engineer", "qa")
    graph.add_edge("qa", "code_reviewer")

    #Review Conditional Routing

    graph.add_conditional_edges(
        "code_reviewer",
        route_after_code_review,
        {
            "backend_dev": "backend_dev",
            "documentation": "documentation",
        },
    )

    #Final Output

    graph.add_edge("documentation", END)

    #Compile Graph

    app = graph.compile()

    logger.info("Graph compiled successfully")
    return app

def run_graph(initial_state: AgenticState):
    """
    Convenience runner with validation.
    """

    validate_initial_state(initial_state)
    app = build_graph()
    logger.info("Starting graph execution")

    final_state = app.invoke(initial_state)
    logger.info("Graph execution completed")

    return final_state