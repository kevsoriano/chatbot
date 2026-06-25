import os
import functions_framework
from dotenv import load_dotenv
from langchain.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent 

# 1. Global Initialization (runs once during cold start)
load_dotenv()
gemini_model = os.getenv("GEMINI_MODEL", "gemini-3.5-flash")

model = ChatGoogleGenerativeAI(model=gemini_model)
agent = create_agent(model=model)

# 2. HTTP-triggered function
@functions_framework.http
def process_request(request):
    """Responds to HTTP requests by passing the input prompt to the AI agent."""
    
    # Parse the request body for the user's prompt or question
    request_json = request.get_json(silent=True)
    request_args = request.args

    # Check for a 'prompt' or 'message' key, default to a generic greeting if not found
    if request_json and 'prompt' in request_json:
        user_prompt = request_json['prompt']
    elif request_args and 'prompt' in request_args:
        user_prompt = request_args['prompt']
    else:
        user_prompt = "Hello my name is Seán and my favourite colour is green"

    try:
        # Wrap the string into a LangChain HumanMessage
        question = HumanMessage(content=user_prompt)
        
        # Invoke the AI Agent
        response = agent.invoke({"messages": [question]})
        
        # Extract the content from the response object
        # Depending on your `create_agent` output structure, you might need response.content or response['output']
        if hasattr(response, 'content'):
            ai_output = response.content
        elif isinstance(response, dict) and 'output' in response:
            ai_output = response['output']
        else:
            ai_output = str(response)

        # Return the AI's answer and a 200 OK status
        return {"response": ai_output}, 200

    except Exception as e:
        # Catch and return errors cleanly
        return {"error": str(e)}, 500