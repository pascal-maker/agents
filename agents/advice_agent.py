"""
Defines the AdviceBot Agent for energy-saving and advice-related questions.
"""
from agentarium import Agent, Action
from utils.langflow_api import query_langflow

advice_agent = Agent.create_agent(name="AdviceBot", occupation="Energy Consultant")

advice_agent.add_action(
    Action(
        name="QUERY_LANGFLOW",
        description="Query Langflow for energy-saving and advice questions",
        parameters=["prompt"],
        function=query_langflow,
    )
)