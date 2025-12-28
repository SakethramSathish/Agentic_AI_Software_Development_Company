"""
LangGraph node definitions.

Each node is a thin wrapper around exactly ONE agent.
NO business logic should exist here.
"""

from typing import Callable

from graph.state import AgenticState

#Import all agent functions

from agents.ceo_agent import ceo_agent
from agents.product_manager_agent import product_manager_agent
from agents.system_architect_agent import system_architect_agent
from agents.cto_agent import cto_agent

from agents.backend_dev_agent import backend_dev_agent
from agents.frontend_dev_agent import frontend_dev_agent
from agents.ai_engineer_agent import ai_engineer_agent

from agents.qa_agent import qa_agent
from agents.code_reviewer_agent import code_reviewer_agent
from agents.documentation_agent import documentation_agent

#Node wrappers

def ceo_node(state: AgenticState) -> AgenticState:
    return ceo_agent(state)

def product_manager_node(state: AgenticState) -> AgenticState:
    return product_manager_agent(state)

def system_architect_node(state: AgenticState) -> AgenticState:
    return system_architect_agent(state)

def cto_node(state: AgenticState) -> AgenticState:
    return cto_agent(state)

def backend_dev_node(state: AgenticState) -> AgenticState:
    return backend_dev_agent(state)

def frontend_dev_node(state: AgenticState) -> AgenticState:
    return frontend_dev_agent(state)

def ai_engineer_node(state: AgenticState) -> AgenticState:
    return ai_engineer_agent(state)

def qa_node(state: AgenticState) -> AgenticState:
    return qa_agent(state)

def code_reviewer_node(state: AgenticState) -> AgenticState:
    return code_reviewer_agent(state)

def documentation_node(state: AgenticState) -> AgenticState:
    return documentation_agent(state)

#Node registry (for debugging/visualization)

NODE_REGISTRY: dict[str, Callable[[AgenticState], AgenticState]] = {
    "ceo": ceo_node,
    "product_manager": product_manager_node,
    "system_architect": system_architect_node,
    "cto": cto_node,
    "backend_dev": backend_dev_node,
    "frontend_dev": frontend_dev_node,
    "ai_engineer": ai_engineer_node,
    "qa": qa_node,
    "code_reviewer": code_reviewer_node,
    "documentation": documentation_node,
}