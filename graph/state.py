from typing import Optional
from pydantic import BaseModel, Field

class AgenticState(BaseModel):
    """
    Global shared state for the Agentic AI Software Company.

    RULES:
    - All agents MUST read/write only fields defined here
    - No agent should invent new state keys
    """
    #User Input and Planning

    user_input: str = Field(..., description="Original user idea / requirement")

    project_brief: Optional[str] = Field(
        default=None, description="Structured project brief from CEO agent"
    )

    product_spec: Optional[str] = Field(
        default=None, description="Product requirements from PM agent"
    )

    architecture_plan: Optional[str] = Field(
        default=None, description="System architecture from Architecture agent"
    )

    #Executive Decisions

    cto_decision: Optional[str] = Field(
        default=None, description="CTO decision: approve | reject"
    )

    #Development Outputs

    backend_code: Optional[str] = Field(
        default=None, description="Backend design/code from Backend Dev agent"
    )

    frontend_code: Optional[str] = Field(
        default=None, description="Streamlit UI code from Frontend Dev agent"
    )

    ai_design_notes: Optional[str] = Field(
        default=None, description="AI strategy notes from AI Engineer agent"
    )

    #Quality Control

    qa_report: Optional[str] = Field(
        default=None, description="QA findings and issues"
    )

    code_review_report: Optional[str] = Field(
        default=None, description="Code review feedback"
    )

    #Documentation & Final Output

    documentation: Optional[str] = Field(
        default=None, description="Generated project documentation"
    )

    final_summary: Optional[str] = Field(
        default=None, description="Final consolidated output for UI"
    )

    #Control and Meta

    review_attempts: int = Field(
        default=0, description="Number of QA/Review retry attempts"
    )