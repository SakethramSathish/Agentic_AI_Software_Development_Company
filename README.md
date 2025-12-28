# Agentic AI Software Development Company

An end-to-end example that simulates a software development company using a collection of role-based AI agents orchestrated by a LangGraph workflow and powered by Google Gemini.

---

## Overview

This project demonstrates an "agentic" system that models the roles inside a software development company (CEO, Product Manager, Architect, CTO, Developers, QA, Code Review, Documentation, etc.). Each role is implemented as a thin agent that uses a centralized Gemini client to generate structured outputs. The agents are composed into a directed workflow using LangGraph.

Key ideas:
- Role-based agents produce incremental artifacts (project brief, product spec, architecture, code sketches, QA & review reports).
- A shared `AgenticState` (Pydantic model) holds the global data each agent reads and writes.
- Conditional routing (CTO decision, review retries) controls the graph flow.

## Features

- Streamlit-based UI entrypoint to submit an idea and run the agentic workflow.
- Centralized Gemini client wrapper for model configuration and safe generation.
- Clear prompt separation via `llm/prompts.py` to keep agent instructions stable.
- LangGraph-driven execution with conditional edges and a final documentation step.

## Quickstart

1. Create and activate a Python environment (recommended):

```bash
python -m venv .venv

# Windows
.\.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your Gemini API key:

```
GEMINI_API_KEY=your_gemini_api_key_here
```

4. Run the Streamlit app:

```bash
streamlit run app.py
```

Open the URL Streamlit prints to the terminal (usually http://localhost:8501).

## Configuration

- See [config/settings.py](config/settings.py) for configuration values used by the system (model names, project metadata, logging, and retry limits).
- The project expects `GEMINI_API_KEY` in the environment; `python-dotenv` is used to load `.env`.

## Architecture & How It Works

High level flow:

1. UI (`app.py`) accepts a textual idea from the user and constructs an `AgenticState`.
2. `graph/graph_builder.py` builds a LangGraph `StateGraph` composed of nodes mapped to agent functions in `agents/`.
3. Each node invokes exactly one agent which may call the centralized `GeminiClient` in `llm/gemini_client.py`.
4. Agents write structured outputs back to the shared `AgenticState` (a Pydantic model in `graph/state.py`).
5. Conditional edges in `graph/edges.py` handle CTO approval and review retry logic.
6. The final output is consolidated and displayed in the Streamlit UI.

Important files:

- [app.py](app.py) — Streamlit UI and orchestration entrypoint
- [config/settings.py](config/settings.py) — environment and model settings
- [llm/gemini_client.py](llm/gemini_client.py) — centralized Gemini wrapper
- [llm/prompts.py](llm/prompts.py) — role-specific system prompts
- [graph/graph_builder.py](graph/graph_builder.py) — graph assembly and runner
- [graph/state.py](graph/state.py) — shared `AgenticState` (Pydantic)
- [graph/nodes.py](graph/nodes.py) — node wrappers mapping to agents
- [graph/edges.py](graph/edges.py) — conditional routing logic
- [agents/](agents/) — role agent implementations (CEO, PM, Architect, CTO, Backend, Frontend, AI Engineer, QA, Code Review, Documentation)
- [utils/logger.py](utils/logger.py) — simple logging setup
- [utils/validators.py](utils/validators.py) — input/state validators

## Agents (summary)

- `ceo_agent` — converts raw user input into a structured project brief.
- `product_manager_agent` — turns the brief into product requirements, features, and acceptance criteria.
- `system_architect_agent` — designs architecture and API boundaries.
- `cto_agent` — reviews architecture and returns a JSON decision (`approve`/`reject`).
- `backend_dev_agent` — generates a FastAPI-style backend skeleton and DB suggestions.
- `frontend_dev_agent` — generates a Streamlit UI skeleton and connects conceptually to backend APIs.
- `ai_engineer_agent` — reviews LLM usage and suggests prompt and memory designs.
- `qa_agent` — performs QA checks against product requirements.
- `code_reviewer_agent` — performs a code review and suggests improvements.
- `documentation_agent` — consolidates outputs into final documentation.

## Development Notes

- Prompts are centralized to avoid drift and keep agent responsibilities explicit (`llm/prompts.py`).
- `GeminiClient` wraps the `google-generativeai` library and enforces simple validation and error handling.
- `AgenticState` defines the schema all agents must use; agents must not invent new state keys.
- Conditional routing limits retries using `MAX_REVIEW_RETRIES` in settings to avoid infinite loops.

## Troubleshooting

- Missing API key: ensure `GEMINI_API_KEY` is present in `.env` or the environment — `config/settings.py` will raise an error otherwise.
- If LangGraph or LangChain APIs change, node signatures or graph compilation could break; keep pinned dependency versions in `requirements.txt`.

## Next Steps & Suggestions

- Add example inputs and expected outputs to `examples/` (not included).
- Add unit tests for `graph/edges.py` and `utils/validators.py`.
- Add a small integration test that runs the graph with a mocked Gemini client.

## License

This project is licensed under the GNU General Public License v3.0 (GPL-3.0). Add a `LICENSE` file containing the full GPL-3.0 text (or use the SPDX identifier `GPL-3.0-or-later`) if you intend to publish the project.

---

