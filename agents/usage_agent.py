from agentarium import Agent, Action
from utils.langflow_api import query_langflow

# Create the Usage Insights Agent
usage_agent = Agent.create_agent(name="UsageBot", occupation="Energy Insights Assistant")

# Add an action that queries Langflow for usage-related questions
usage_agent.add_action(
    Action(
        name="QUERY_LANGFLOW",
        description="Handles customer queries related to energy consumption and usage insights via Langflow.",
        parameters=["prompt"],
        function=query_langflow
    )
)
