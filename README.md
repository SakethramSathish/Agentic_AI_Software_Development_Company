# Agentic AI Software Development Company

![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=FastAPI&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-000000?style=for-the-badge&logo=langchain&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini-8E75B2?style=for-the-badge&logo=googlebard&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

An end-to-end example that simulates a software development company using a collection of role-based AI agents. Orchestrated by a **LangGraph workflow**, powered by **Google Gemini**, and visualised through a stunning **Neo-Brutalist React Dashboard**.

---

## 🌟 Overview

This project demonstrates an "agentic" system that models the roles inside a complete software development company (CEO, Product Manager, Architect, CTO, Developers, QA, Code Review, Documentation). 

Each role is a targeted AI agent that uses a centralized Gemini client to generate structured outputs. The agents are composed into a directed workflow using LangGraph, and their live progress is streamed to a dynamic React frontend using **Server-Sent Events (SSE)**.

## ✨ Features

- **Neo-Brutalist React Dashboard**: A custom frontend built with Vite, Tailwind CSS, and Framer Motion featuring a dark cyan theme, bold typography, and interactive pipeline visualizations.
- **Real-Time Agent Streaming**: FastAPI backend streams each agent's status and outputs live to the user interface via SSE.
- **Centralized Gemini Client**: Shared LLM wrapper for consistent model configuration and safe generation across all agents.
- **Strict Role-Based Prompts**: Clear prompt separation via `llm/prompts.py` ensures agent instructions remain perfectly aligned with their organizational roles.
- **LangGraph Driven Execution**: Conditional state edges control the graph flow (e.g., the CTO deciding whether to approve the Architecture before moving to Development).

---

## 🏗️ Tech Stack

### Frontend
- **React 18** (Vite)
- **Tailwind CSS v3** (Custom Neo-Brutalist design tokens)
- **Framer Motion** (Micro-interactions and pipeline animations)
- **React Markdown** & **Syntax Highlighter** (Output rendering)

### Backend
- **Python 3.10+**
- **FastAPI** & **Uvicorn** (REST APIs and SSE streaming)
- **LangGraph** (Workflow orchestration)
- **Google Gemini** (LLM operations)

---

## 🚀 Quickstart

### 1. Backend Setup

Open a terminal and set up the Python backend.

```bash
# Create a virtual environment (recommended)
python -m venv .venv

# Activate it (Windows)
.\.venv\Scripts\activate
# Activate it (macOS/Linux)
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

Create a `.env` file in the root directory and add your Gemini API key:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

Start the FastAPI server:
```bash
uvicorn server:app --reload --port 8000
```

### 2. Frontend Setup

Open a **separate terminal** and navigate to the `frontend` folder.

```bash
cd frontend

# Install Node dependencies
npm install

# Start the Vite development server
npm run dev
```

The UI should now be running at **http://localhost:5173**.

---

## 🧠 Architecture & Flow

High-level application flow:

1. The user inputs their software idea via the **React Dashboard**.
2. The UI sends a POST request to `server.py`, starting the pipeline.
3. `graph/stream_runner.py` builds the LangGraph `StateGraph` mapped to the agents and begins `stream()` execution.
4. As each agent finishes, the backend yields an **SSE chunk** (`event: agent_update`) to the frontend in real-time.
5. The React `PipelineVisualizer` updates, animating the agent nodes. 
6. Conditional edges handle internal iteration (e.g. CTO approval, code review retries).
7. Upon completion (`event: complete`), the final project documentation is rendered in the dashboard.

### Important Directories & Files

- `server.py` — FastAPI application and entry point.
- `frontend/` — The React UI application.
- `graph/stream_runner.py` — LangGraph pipeline stream handler.
- `graph/state.py` — Shared `AgenticState` Pydantic model dictating what keys agents can read/write.
- `agents/` — Implementation logic for the 10 role-based agents.
- `llm/prompts.py` — Centralized prompt library for the LLM profiles.

---

## 👥 The Agents

1. **CEO** (`ceo_agent`) — Converts raw input into a project brief.
2. **Product Manager** (`product_manager_agent`) — Formulates product requirements and specs.
3. **System Architect** (`system_architect_agent`) — Designs the system architecture.
4. **CTO** (`cto_agent`) — Reviews architecture. Makes a binary `approve/reject` decision modifying the graph flow.
5. **Backend Developer** (`backend_dev_agent`) — Generates backend code scaffolding.
6. **Frontend Developer** (`frontend_dev_agent`) — Generates UI interface concepts.
7. **AI Engineer** (`ai_engineer_agent`) — Analyzes and designs LLM/prompting integration.
8. **QA Engineer** (`qa_agent`) — Cross-checks the implementations against the product requirements.
9. **Code Reviewer** (`code_reviewer_agent`) — Evaluates code quality, potentially triggering a retry loop.
10. **Documentation** (`documentation_agent`) — Consolidates the outputs into professional Markdown docs.

---

## 🛠️ Development Notes

- **Prompts**: Keep prompts strictly segregated in `llm/prompts.py`. Never inline them to maintain role-play clarity.
- **Shared State**: All agents use `AgenticState`. If you add a new data format, update the state definition first.
- **Port Matching**: Remember that Vite is proxying API requests to `localhost:8000`. Ensure FastAPI remains on port 8000 when developing locally.
