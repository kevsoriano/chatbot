from vertexai.agent_engines import LanggraphAgent
from tools.researcher_tools import web_search

orchestrator_agent = LanggraphAgent(
    """Determines if the query is conversational or requires data retrieval"""
    model="gemini-3.5-flash",
    system_prompt="You are a research agent. Your task is to gather information and provide concise summaries.",
)

def orchestrator_node(state):
    # Extract the latest message from the state
    latest_message = state["messages"][-1] if state["messages"] else None

    if latest_message:
        # Use the orchestrator agent to determine the next agent
        response = orchestrator_agent.query(
            input=latest_message.content,
        )
        # Update the state with the next agent based on the orchestrator's decision
        state["next_agent"] = response  
    else:
        state["next_agent"] = "" 

    return state