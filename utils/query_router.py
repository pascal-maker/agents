from agents.billing_agent import billing_agent
from agents.usage_agent import usage_agent
from agents.advice_agent import advice_agent

def route_customer_query(query: str):
    """
    Routes the customer query to the appropriate agent and sends it to Langflow.
    """
    query_lower = query.lower()

    if "bill" in query_lower or "payment" in query_lower:
        response = billing_agent.execute_action("QUERY_LANGFLOW", query)
    elif "usage" in query_lower or "consumption" in query_lower:
        response = usage_agent.execute_action("QUERY_LANGFLOW", query)
    elif "save" in query_lower or "reduce" in query_lower:
        response = advice_agent.execute_action("QUERY_LANGFLOW", query)
    else:
        response = {"response": "I'm not sure which category this belongs to."}

    return response
