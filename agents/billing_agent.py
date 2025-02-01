"""
Defines the BillingBot Agent for billing-related questions.
"""
from agentarium import Agent, Action
from utils.langflow_api import query_langflow

billing_agent = Agent.create_agent(name="BillingBot", occupation="Billing Specialist")

billing_agent.add_action(
    Action(
        name="QUERY_LANGFLOW",
        description="Query Langflow for billing-related questions",
        parameters=["prompt"],
        function=query_langflow,
    )
)