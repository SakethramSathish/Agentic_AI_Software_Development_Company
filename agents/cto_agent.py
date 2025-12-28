import json

from llm.gemini_client import GeminiClient
from llm.prompts import CTO_SYSTEM_PROMPT
from graph.state import AgenticState

def cto_agent(state: AgenticState) -> AgenticState:
    """
    CTO Agent

    Responsibilities:
    - Review system architecture
    - Approve or reject the plan
    - Provide a clear reason
    """

    if not state.architecture_plan:
        raise ValueError(
            "Architecture plan missing. System Architect agent must run first."
        )
    
    client = GeminiClient(model_type="fast")

    prompt = f"""
Proposed Architecture:
{state.architecture_plan}

Review the architecture and decide whether it is technically sound.
"""
    
    response = client.generate(
        prompt=prompt,
        system_instruction=CTO_SYSTEM_PROMPT,
        temperature=0.2
    )

    try:
        decision_payload = json.loads(response)
        decision = decision_payload.get("decision")
        reason = decision_payload.get("reason")

        if decision not in {"approve", "reject"}:
            raise ValueError("Invalid CTO decision value.")
        
    except Exception as e:
        raise RuntimeError(
            f"CTO response parsing failed. Raw response:\n{response}"
        ) from e
    
    #Update State
    state.cto_decision = decision

    #Append decision context to architecture plan (traceability)
    state.architecture_plan += f"\n\nCTO Decision: {decision.upper()}\nReason: {reason}"
    
    return state