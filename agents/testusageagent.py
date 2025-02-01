"""
Defines the UsageAgent for Luminus usage-related questions:
- Why is my usage high/low?
- Historical data or peak usage periods
- Possibly references a usage database or CSV content
"""

from agentarium import Agent, Action

def explain_usage(query: str, **kwargs) -> str:
    """
    Provide a generic usage explanation or tips based on the CSV content.
    In a real system, this might query historical usage data, peak consumption, etc.
    """
    # Example simplistic logic
    return (
        "Op basis van je historische data zien we dat je verbruik hoger was in "
        "deze periode vanwege koude temperaturen of piekuren.\n"
        "Om je verbruik te verlagen, kun je piekverbruik spreiden. "
        "Bekijk ook regelmatig je meterstanden via My Luminus."
    )

testusage_agent = Agent.create_agent(name="UsageAgent", occupation="Energy Usage Analyst")

testusage_agent.add_action(
    Action(
        name="EXPLAIN_USAGE",
        description="Explain customer's usage patterns referencing CSV data",
        parameters=["query"],
        function=explain_usage,
    )
)
