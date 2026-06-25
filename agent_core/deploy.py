import vertexai
from config import PROJECT_ID, LOCATION, STAGING_BUCKET
from graph import compiled_graph

vertexai.init(project=PROJECT_ID, location=LOCATION)
client = vertexai.Client(project=PROJECT_ID, location=LOCATION)

remote_agent = client.agent_engines.create(
    agent=compiled_graph,  # Pushing the master multi-agent graph
    config={
        "staging_bucket": STAGING_BUCKET,
        "requirements": ["langchain-core", "langgraph"],
    }
)
print(f"Multi-agent engine deployed successfully: {remote_agent.api_resource.name}")