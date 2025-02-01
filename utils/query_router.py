"""
Routes the customer query to the appropriate agent
based on simple keyword matching.
"""

from agents.billing_agent import billing_agent
from agents.usage_agent import usage_agent
from agents.advice_agent import advice_agent

def route_customer_query(query: str):
    """
    Routes the user query to the most appropriate agent based on keywords.
    """
    query_lower = query.lower()
    print(f"🔵 Routing query: {query}")

    # Billing Agent
    if any(word in query_lower for word in ["factuur", "betaling", "rekening",
                                            "voorschot", "prijs", "tarief"]):
        print("🟢 Billing Agent Selected")
        response = billing_agent.execute_action("QUERY_LANGFLOW", query)

    # Usage Agent
    elif any(word in query_lower for word in ["energie", "verbruik", "consumptie", "hoeveel"]):
        print("🟢 Usage Agent Selected")
        response = usage_agent.execute_action("QUERY_LANGFLOW", query)

    # Advice Agent
    elif any(word in query_lower for word in ["besparen", "verminderen", "optimaliseren", "advies"]):
        print("🟢 Advice Agent Selected")
        response = advice_agent.execute_action("QUERY_LANGFLOW", query)

    # If no match is found
    else:
        print("🚨 Query did not match any category!")
        response = {"response": "I'm not sure which category this belongs to."}

    print(f"🔵 Langflow Response: {response}")  # DEBUG
    return response