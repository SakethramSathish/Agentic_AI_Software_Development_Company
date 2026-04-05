"""
FastAPI backend server for the Agentic AI Software Development Company.
Replaces the Streamlit frontend with a REST + SSE API.
"""

import asyncio
import json

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel

from graph.stream_runner import stream_graph
from utils.logger import setup_logger

logger = setup_logger(__name__)

# ─── App Setup ───────────────────────────────────────────────

app = FastAPI(
    title="Agentic AI Software Company API",
    version="1.0.0",
    description="AI-powered software development pipeline using Gemini + LangGraph",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ─── Request Models ──────────────────────────────────────────

class IdeaRequest(BaseModel):
    idea: str


# ─── Endpoints ───────────────────────────────────────────────

@app.get("/api/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "ok", "service": "agentic-ai-company"}


@app.post("/api/run")
async def run_pipeline(request: IdeaRequest):
    """
    Run the full agentic pipeline and stream results via SSE.
    Each agent completion emits an event with the agent name and output.
    """
    if not request.idea.strip():
        raise HTTPException(status_code=400, detail="Idea cannot be empty.")

    logger.info(f"Pipeline triggered with idea: {request.idea[:80]}...")

    async def event_stream():
        queue = asyncio.Queue()
        loop = asyncio.get_event_loop()

        def _run_sync():
            """Run the synchronous LangGraph pipeline in a background thread."""
            try:
                for event in stream_graph(request.idea):
                    asyncio.run_coroutine_threadsafe(
                        queue.put(("agent", event)), loop
                    )
                asyncio.run_coroutine_threadsafe(
                    queue.put(("done", None)), loop
                )
            except Exception as e:
                logger.exception("Pipeline execution failed")
                asyncio.run_coroutine_threadsafe(
                    queue.put(("error", str(e))), loop
                )

        # Start sync pipeline in a background thread
        loop.run_in_executor(None, _run_sync)

        while True:
            msg_type, data = await queue.get()

            if msg_type == "agent":
                yield f"event: agent_update\ndata: {json.dumps(data)}\n\n"
            elif msg_type == "done":
                yield f"event: complete\ndata: {json.dumps({'status': 'done'})}\n\n"
                break
            elif msg_type == "error":
                yield f"event: error\ndata: {json.dumps({'error': data})}\n\n"
                break

    return StreamingResponse(
        event_stream(),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )
