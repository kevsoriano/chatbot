from google.adk.agents import Agent
from vertexai.agent_engines import LanggraphAgent

orchestrator_config = Agent(
    name="orchestrator_agent",
    model="gemini-2.5-flash", 
    system_instruction="You are a orchestrator agent. Your task is to gather information and provide concise summaries.",
)

orchestrator_agent = LanggraphAgent(
    agent=orchestrator_config
)

def orchestrator_node(state):
    # Extract the latest message from the state
    latest_message = state["messages"][-1] if state["messages"] else None

    # Use the orchestrator agent to determine the next agent
    response = orchestrator_agent.query(
        input=latest_message.content,
    )
    # Update the state with the next agent based on the orchestrator's decision
    state["next_agent"] = response  

    return state