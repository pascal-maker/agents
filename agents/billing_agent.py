from agentarium import Agent, Action
from utils.langflow_api import query_langflow

# Create the Billing Agent
billing_agent = Agent.create_agent(name="BillingBot", occupation="Billing Specialist")

# Add an action that queries Langflow for billing-related questions
billing_agent.add_action(
    Action(
        name="QUERY_LANGFLOW",
        description="Handles customer queries related to billing via Langflow.",
        parameters=["prompt"],
        function=query_langflow
    )
)
