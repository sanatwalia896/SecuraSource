import streamlit as st
import subprocess
from typing import TypedDict

from utils.system_monitor import SystemMonitor
from utils.vector_store import create_vector_store

from agents.documentation_agent import DocumentationAgent
from agents.command_flow_agent import CommandFlowAgent
from agents.system_monitor_agent import SystemMonitorAgent
from agents.code_review_agent import CodeReviewAgent
from agents.execution_agent import ExecutionAgent
from agents.report_agent import ReportAgent

from langgraph.graph import StateGraph, END
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from config import Config

# Global system monitor object
monitor = SystemMonitor()


# --- Agent State ---
class AgentState(TypedDict):
    repo_path: str
    vector_store: object
    documents: list
    doc_analysis: str
    command_flow: str
    system_changes: str
    code_review: str
    execution_results: str
    final_report: str


# --- Node Functions ---
def setup_vector_store(state: AgentState):
    vector_store, documents = create_vector_store(state["repo_path"])
    return {"vector_store": vector_store, "documents": documents}

def run_doc_agent(state: AgentState):
    agent = DocumentationAgent(state["vector_store"])
    return {"doc_analysis": agent.analyze_docs()}

def run_command_agent(state: AgentState):
    agent = CommandFlowAgent(state["vector_store"])
    return {"command_flow": agent.generate_commands()}

def run_monitor_agent(state: AgentState):
    try:
        changes = monitor.get_changes()
    except Exception as e:
        return {"system_changes": f"Error fetching system changes: {e}"}

    prompt = ChatPromptTemplate.from_template(
        "Analyze these system changes after software execution:\n{changes}"
    )
    llm = ChatGroq(api_key=Config.GROQ_API_KEY, model=Config.MODEL)
    response = llm.invoke(prompt.format(changes=str(changes)))

    return {"system_changes": response.content}

def run_code_review(state: AgentState):
    agent = CodeReviewAgent(state["vector_store"])
    return {"code_review": agent.review_code()}

def run_execution(state: AgentState):
    agent = ExecutionAgent(state["command_flow"])
    return {"execution_results": agent.execute()}

def run_report_agent(state: AgentState):
    agent = ReportAgent()
    report = agent.generate_report(
        state["doc_analysis"],
        state["command_flow"],
        state["system_changes"],
        state["code_review"],
        state["execution_results"]
    )
    return {"final_report": report}


# --- LangGraph Workflow ---
def create_workflow():
    workflow = StateGraph(AgentState)

    workflow.add_node("setup_vector_store", setup_vector_store)
    workflow.add_node("doc_agent", run_doc_agent)
    workflow.add_node("command_agent", run_command_agent)
    workflow.add_node("monitor_agent", run_monitor_agent)
    workflow.add_node("code_review_node", run_code_review)
    workflow.add_node("execution", run_execution)
    workflow.add_node("report", run_report_agent)

    workflow.set_entry_point("setup_vector_store")

    workflow.add_edge("setup_vector_store", "doc_agent")
    workflow.add_edge("setup_vector_store", "command_agent")
    workflow.add_edge("setup_vector_store", "code_review_node")

    workflow.add_edge("command_agent", "execution")
    workflow.add_edge("execution", "monitor_agent")
    workflow.add_edge("monitor_agent", "report")

    workflow.add_edge("code_review_node", "report")
    workflow.add_edge("doc_agent", "report")
    workflow.add_edge("report", END)

    return workflow.compile()


# --- Streamlit App UI ---
def main():
    st.title("🛡️ Open Source Vulnerability Detection")
    st.markdown("Analyze open-source repos for risky patterns using LLM agents 🔍")

    repo_url = st.text_input("🔗 Enter Git Repository URL:")

    if st.button("🚀 Analyze Repository"):
        if repo_url:
            repo_path = "./data/repos/temp_repo"
            subprocess.run(f"rm -rf {repo_path}", shell=True)  # Cleanup old repo if any
            subprocess.run(f"git clone {repo_url} {repo_path}", shell=True)

            monitor.capture_initial_state()

            workflow = create_workflow()

            initial_state = AgentState(
                repo_path=repo_path,
                vector_store=None,
                documents=[],
                doc_analysis="",
                command_flow="",
                system_changes="",
                code_review="",
                execution_results="",
                final_report=""
            )

            result = workflow.invoke(initial_state)

            st.subheader("🧾 Vulnerability Report")
            st.markdown(result["final_report"])

            subprocess.run(f"rm -rf {repo_path}", shell=True)
        else:
            st.error("⚠️ Please enter a valid Git repository URL.")


if __name__ == "__main__":
    main()
