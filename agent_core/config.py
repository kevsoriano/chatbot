import vertexai

# 1. Initialization
PROJECT_ID = "dev-sandbox-kevingil"
LOCATION = "us-central1" 
STAGING_BUCKET = f"gs://{PROJECT_ID}-agent-engine-staging"

vertexai.init(project=PROJECT_ID, location=LOCATION)