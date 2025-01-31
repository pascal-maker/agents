"""
Handles the API call to Langflow using a prompt. Make sure you have a .env with ASTRA_DB_APPLICATION_TOKEN.
"""

import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

BASE_API_URL = "https://api.langflow.astra.datastax.com"
LANGFLOW_ID = "01375dcf-c094-4a69-9370-bc9c86149df0"
APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")  # Must be set in .env
ENDPOINT = "customer"  # Adjust if needed

def query_langflow(
    prompt: str, 
    endpoint: str = ENDPOINT, 
    output_type: str = "chat", 
    input_type: str = "chat", 
    **kwargs
) -> dict:
    """
    Calls the Langflow API using the given prompt and returns the JSON response.
    Extra kwargs are ignored or can be used if needed.
    """
    if not APPLICATION_TOKEN:
        print("🚨 ERROR: ASTRA_DB_APPLICATION_TOKEN is missing or not set!")
        return {"error": "ASTRA_DB_APPLICATION_TOKEN is missing. Please set it in the .env file."}
    
    try:
        api_url = f"{BASE_API_URL}/lf/{LANGFLOW_ID}/api/v1/run/{endpoint}"
        payload = {
            "input_value": prompt,
            "output_type": output_type,
            "input_type": input_type,
        }
        headers = {
            "Authorization": f"Bearer {APPLICATION_TOKEN}",
            "Content-Type": "application/json",
        }

        print(f"🔵 Sending API request to: {api_url}")
        print(f"🟡 Payload: {payload}")  # Debug logs

        response = requests.post(api_url, json=payload, headers=headers)
        response_data = response.json()

        print(f"🟢 Langflow API Response: {response_data}")  # Debug logs
        return response_data

    except Exception as e:
        return {"error": f"Langflow query failed: {str(e)}"}
