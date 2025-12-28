"""
LangGraph edge routing logic.

This file defines:
- Conditional routing decisions
- Retry / loop behavior
- Clear next-node selection
"""

from graph.state import AgenticState
from config.settings import MAX_REVIEW_RETRIES

#CTO decision routing

def route_after_cto(state: AgenticState) -> str:
    """
    Decide where to go after CTO review.

    Returns:
        Next node name
    """
    if state.cto_decision == "approve":
        return "backend_dev"
    elif state.cto_decision == "reject":
        return "system_architect"
    else:
        raise ValueError(
            f"Invalid CTO decision in state: {state.cto_decision}"
        )
    
#QA/Review Routing

def route_after_code_review(state: AgenticState) -> str:
    """
    Decide whether to retry development or proceed to documentation.

    Uses review_attempts to prevent infinite loops.
    """

    if state.review_attempts >- MAX_REVIEW_RETRIES:
        #Force forward progress
        return "documentation"
    
    if state.qa_report or state.code_review_report:
        state.review_attempts += 1
        return "backend_dev"
    
    return "documentation"