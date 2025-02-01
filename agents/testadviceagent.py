"""
Defines the AdviceAgent for providing energy-saving advice, tips, 
and general guidance drawn from the CSV content.
"""

from agentarium import Agent, Action

def provide_energy_advice(query: str, **kwargs) -> str:
    """
    Provide energy-saving tips or advice. Could incorporate specific 
    data (like capacity tariffs or new insulation suggestions).
    """
    # This is a simplified example referencing the CSV summary info.
    advice = [
        "Schakel elektrische toestellen volledig uit i.p.v. op stand-by.",
        "Overweeg om piekverbruik te spreiden buiten de drukke uren.",
        "Controleer isolatie en denk aan zonnepanelen of warmtepomp.",
        "Monitor je verbruik via My Luminus om beter inzicht te krijgen."
    ]
    joined_advice = "\n• ".join(advice)
    return f"Hier zijn enkele algemene tips om energie te besparen:\n• {joined_advice}"

testadvice_agent = Agent.create_agent(name="AdviceAgent", occupation="Energy Advisor")

testadvice_agent.add_action(
    Action(
        name="PROVIDE_ENERGY_ADVICE",
        description="Provide tips for reducing energy consumption and saving costs",
        parameters=["query"],
        function=provide_energy_advice,
    )
)
