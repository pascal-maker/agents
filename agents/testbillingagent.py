"""
Defines the BillingAgent for Luminus billing-related questions,
including capacity tariffs, billing cycles, and paying methods.
Utilizes custom actions to handle billing queries.
"""

from agentarium import Agent, Action

# Example: A custom function that references billing guidelines from your summary CSV content
def provide_billing_explanation(query: str, **kwargs) -> str:
    """
    Provide an explanation about why a customer's bills or
    monthly installments (voorschotten) might be higher or lower,
    referencing your CSV content. This can be expanded with real data lookups.
    """
    # Very basic logic — in reality, you'd parse the query, check database, etc.
    if "voorschotten" in query.lower():
        return (
            "Bij de berekening van je nieuwe voorschotten houden we rekening "
            "met gegevens zoals verwachte verbruik (bijv. normale winter, prijzen op de groothandel, etc.).\n"
            "Zelfs als je geld terugkrijgt, kan het zijn dat de voorschotten omhooggaan "
            "als we een hogere verwachting hebben voor volgend jaar. "
            "Je kunt je voorschotbedrag zelf aanpassen in My Luminus."
        )
    else:
        return (
            "Ik zie dat je een vraag hebt over je factuur of voorschotten. "
            "Kun je iets meer toelichten zodat ik je gerichter kan helpen? "
            "Je kunt ook My Luminus raadplegen voor een directe aanpassing."
        )

# Create the BillingAgent
testbilling_agent = Agent.create_agent(name="BillingAgent", occupation="Billing Specialist")

# Add a custom action for providing billing explanations
testbilling_agent.add_action(
    Action(
        name="PROVIDE_BILLING_EXPLANATION",
        description="Provide an explanation referencing CSV summary data for Luminus billing queries",
        parameters=["query"],
        function=provide_billing_explanation,
    )
)

# You can add more actions here. For example:
# - "QUERY_CAPACITY_TARIFF"
# - "APPLY_PAYMENT_METHOD_CHANGE"
# - etc.
