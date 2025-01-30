from langflow.load import run_flow_from_json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Define tweaks for Langflow configuration (if required)
TWEAKS = {
  "ChatInput-49JWE": {},
  "Agent-FKniU": {},
  "Prompt-i2BZR": {},
  "ChatOutput-4liAi": {},
  "AstraDB-pdR0L": {},
  "ParseData-vOQYo": {},
  "File-WDGQE": {},
  "SplitText-G57ix": {},
  "AstraDB-6jGDK": {},
  "Agent-niM4e": {},
  "Agent-eWsck": {},
  "AstraDBToolComponent-X7ML0": {},
  "AstraDBToolComponent-bh6bG": {}
}

def query_langflow(prompt: str, *args, **kwargs):
    """
    Calls the Langflow chatbot hosted in Astra DataStax and retrieves responses.
    """
    try:
        session_id = kwargs.get("session_id", "")

        # Define the absolute path to your JSON file
        json_path = "/Users/pascal-maker/Documents/agents/Customer support agent.json"

        # Ensure the file exists before calling Langflow
        if not os.path.exists(json_path):
            return {"error": f"Langflow JSON file not found at {json_path}"}

        result = run_flow_from_json(
            flow=json_path,  # Use the absolute file path
            input_value=prompt,
            session_id=session_id,
            fallback_to_env_vars=True
        )

        response_text = result.get("outputs", {}).get("response", "No response received.")

        return {"customer_query": prompt, "response": response_text}

    except Exception as e:
        return {"error": f"Langflow query failed: {str(e)}"}