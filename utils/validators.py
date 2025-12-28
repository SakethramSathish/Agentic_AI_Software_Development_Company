from graph.state import AgenticState

def validate_initial_state(state: AgenticState) -> None:
    """
    Validate the initial state before starting the graph.

    Raises:
        ValueError if the state is invalid.
    """
    if not isinstance(state, AgenticState):
        raise ValueError("State must be an instance of AgenticState.")
    
    if not state.user_input or not isinstance(state.user_input, str):
        raise ValueError("user_input must be a non-empty string.")
    
def validate_cto_decision(state: AgenticState) -> None:
    """
    Validate CTO Decision field.

    Raises:
        ValueError if decision is invalid.
    """

    if state.cto_decision is None:
        raise ValueError("CTO decision is missing.")
    
    if state.cto_decision not in {"approve", "reject"}:
        raise ValueError (
            f"Invalid CTO decision: {state.cto_decision}."
            "Expected 'approve' or 'reject'."
        )
    
def validate_dev_outputs(state: AgenticState) -> None:
    """
    Validate development outputs before QA / Review.
    """

    if not state.backend_code:
        raise ValueError("Backend code missing before QA/Review.")
    
    if not state.frontend_code:
        raise ValueError("Frontend code missing before QA/Review.")