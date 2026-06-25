from langgraph.graph import StateGraph, START, END
from state import MultiAgentState
from agents.orchestrator import orchestrator_node

# Initialize the master workflow
workflow = StateGraph(MultiAgentState)

# Add nodes
workflow.add_node("orchestrator", orchestrator_node)

# Define routing/edges
workflow.add_edge(START, "orchestrator")
# (Add your conditional routing logic here based on state["next_agent"])

# Compile the final graph
compiled_graph = workflow.compile()