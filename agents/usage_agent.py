"""
Defines the UsageBot Agent for energy usage-related questions.
"""
from agentarium import Agent, Action
from utils.langflow_api import query_langflow

usage_agent = Agent.create_agent(name="UsageBot", occupation="Energy Insights Assistant")

usage_agent.add_action(
    Action(
        name="QUERY_LANGFLOW",
        description="Query Langflow for energy usage-related questions",
        parameters=["prompt"],
        function=query_langflow,
    )
)
