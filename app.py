<<<<<<< HEAD
import streamlit as st

from graph.graph_builder import run_graph
from graph.state import AgenticState
from utils.logger import setup_logger

#App Setup

st.set_page_config(
    page_title="Agentic AI Software Company",
    page_icon="🏢",
    layout="wide",
)

logger = setup_logger(__name__)

#UI Header

st.title("🏢 Agentic AI Software Development Company")
st.caption(
    "An end-to-end AI system that simulates a real software company using Gemini + LangGraph"
)

st.markdown("---")

#User Input

st.subheader("📝 Describe Your Software Idea")

user_input = st.text_area(
    label="Enter your idea or requirements",
    placeholder="Example: Build an AI-powered study planner for college students...",
    height=150,
)

run_button = st.button("🚀 Build with AI Company")

#Run Agentic System

if run_button:
    if not user_input.strip():
        st.error("Please enter a valid software idea.")
    else:
        logger.info("User triggered agentic workflow")

        with st.spinner("🤖 AI company is working... This may take a minute."):
            try:
                inital_state = AgenticState(user_input=user_input)
                final_state = run_graph(inital_state)

                st.success("✅ Project completed successfully!")

            except Exception as e:
                logger.exception("Graph execution failed")
                st.error(f"❌ Something went wrong:\n\n{str(e)}")
                st.stop()

        #Final Output

        st.markdown("---")
        st.subheader("📘 Final Project Documentation")

        if final_state.get("final_summary"):
            st.markdown(final_state.get("final_summary"))
        else:
            st.warning("No final documentation was generated.")

        #Optional: Detailed Outputs

        with st.expander("🔍 View Detailed Agent Outputs"):

            st.markdown("### 🧠 CEO – Project Brief")
            st.write(final_state.get("project_brief"))

            st.markdown("### 📦 Product Manager – Product Specification")
            st.write(final_state.get("product_spec"))

            st.markdown("### 🏗️ Architect – System Architecture")
            st.write(final_state.get("architecture_plan"))

            st.markdown("### 🧠 CTO – Decision")
            st.write(final_state.get("cto_decision"))

            st.markdown("### 💻 Backend Developer")
            st.code(final_state.get("backend_code") or "", language="python")

            st.markdown("### 🎨 Frontend Developer")
            st.code(final_state.get("frontend_code") or "", language="python")

            st.markdown("### 🤖 AI Engineer Notes")
            st.write(final_state.get("ai_design_notes"))

            st.markdown("### 🧪 QA Report")
            st.write(final_state.get("qa_report"))

            st.markdown("### 🧾 Code Review Report")
=======
import streamlit as st

from graph.graph_builder import run_graph
from graph.state import AgenticState
from utils.logger import setup_logger

#App Setup

st.set_page_config(
    page_title="Agentic AI Software Company",
    page_icon="🏢",
    layout="wide",
)

logger = setup_logger(__name__)

#UI Header

st.title("🏢 Agentic AI Software Development Company")
st.caption(
    "An end-to-end AI system that simulates a real software company using Gemini + LangGraph"
)

st.markdown("---")

#User Input

st.subheader("📝 Describe Your Software Idea")

user_input = st.text_area(
    label="Enter your idea or requirements",
    placeholder="Example: Build an AI-powered study planner for college students...",
    height=150,
)

run_button = st.button("🚀 Build with AI Company")

#Run Agentic System

if run_button:
    if not user_input.strip():
        st.error("Please enter a valid software idea.")
    else:
        logger.info("User triggered agentic workflow")

        with st.spinner("🤖 AI company is working... This may take a minute."):
            try:
                inital_state = AgenticState(user_input=user_input)
                final_state = run_graph(inital_state)

                st.success("✅ Project completed successfully!")

            except Exception as e:
                logger.exception("Graph execution failed")
                st.error(f"❌ Something went wrong:\n\n{str(e)}")
                st.stop()

        #Final Output

        st.markdown("---")
        st.subheader("📘 Final Project Documentation")

        if final_state.get("final_summary"):
            st.markdown(final_state.get("final_summary"))
        else:
            st.warning("No final documentation was generated.")

        #Optional: Detailed Outputs

        with st.expander("🔍 View Detailed Agent Outputs"):

            st.markdown("### 🧠 CEO – Project Brief")
            st.write(final_state.get("project_brief"))

            st.markdown("### 📦 Product Manager – Product Specification")
            st.write(final_state.get("product_spec"))

            st.markdown("### 🏗️ Architect – System Architecture")
            st.write(final_state.get("architecture_plan"))

            st.markdown("### 🧠 CTO – Decision")
            st.write(final_state.get("cto_decision"))

            st.markdown("### 💻 Backend Developer")
            st.code(final_state.get("backend_code") or "", language="python")

            st.markdown("### 🎨 Frontend Developer")
            st.code(final_state.get("frontend_code") or "", language="python")

            st.markdown("### 🤖 AI Engineer Notes")
            st.write(final_state.get("ai_design_notes"))

            st.markdown("### 🧪 QA Report")
            st.write(final_state.get("qa_report"))

            st.markdown("### 🧾 Code Review Report")
>>>>>>> 1e34b23 (Adding frontend)
            st.write(final_state.get("code_review_report"))