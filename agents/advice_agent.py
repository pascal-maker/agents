from agentarium import Agent, Action
from utils.langflow_api import query_langflow

# Create the Energy Advice Agent
advice_agent = Agent.create_agent(name="AdviceBot", occupation="Energy Consultant")

# Add an action that queries Langflow for energy-saving advice
advice_agent.add_action(
    Action(
        name="QUERY_LANGFLOW",
        description="Provides energy-saving recommendations and advice via Langflow.",
        parameters=["prompt"],
        function=query_langflow
    )
)
