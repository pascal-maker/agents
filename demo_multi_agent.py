"""
Multimodal Energy Assistant for Luminus
---------------------------------------

Case Briefing:
- Objective: Demonstrate a multi-agent architecture to handle various energy-related
  customer inquiries (billing, usage, advice, etc.) across multiple channels.
- Each agent has a specialized role. They can "talk" to each other and use .act() to simulate
  internal decision-making. 
- This simple example uses Agentarium's minimal 'talk_to' and 'act' methods to show how agents 
  might collaborate. 
"""

from agentarium import Agent

# 1) System-level or enterprise-level prompt/context (Optional in code snippet)
SYSTEM_PROMPT = """
You are a set of cooperating agents within Luminus, an energy provider. 
Your goals:
1. Provide seamless assistance to customers about billing, usage, and general energy advice.
2. Maintain data privacy/security.
3. Avoid negative statements about Luminus. 
4. Keep the conversation context aware; do not re-ask for personal info if already known.
"""

# 2) Create specialized agents
billing_agent = Agent.create_agent(name="BillingAgent", occupation="Billing Specialist")
usage_agent   = Agent.create_agent(name="UsageAgent", occupation="Energy Usage Analyst")
advice_agent  = Agent.create_agent(name="AdviceAgent", occupation="Energy Advisor")

# 3) Demonstrate internal multi-agent communication
billing_agent.talk_to(
    usage_agent,
    "Hello UsageAgent! The customer wants to know why their latest bill was so high. "
    "Could you share the usage data to see if there's a spike?"
)

usage_agent.talk_to(
    advice_agent,
    "Sure. I've pulled the data and see an increased peak consumption in the evenings. "
    "AdviceAgent, do you have any suggestions to help reduce costs during peak hours?"
)

advice_agent.talk_to(
    billing_agent,
    "Absolutely. Scheduling heavy appliances (dishwasher, laundry) outside peak hours could help. "
    "We can also advise them to check insulation or faulty appliances. Let's share these tips."
)

# 4) Let each agent "act" on their own internal logic
billing_agent.act() 
usage_agent.act()
advice_agent.act()

# 5) Print interactions for debug or logging
print("--- BillingAgent's interactions ---")
print(billing_agent.get_interactions())

print("\n--- UsageAgent's interactions ---")
print(usage_agent.get_interactions())

print("\n--- AdviceAgent's interactions ---")
print(advice_agent.get_interactions())

# This is a basic demonstration of how a multi-agent system could be structured
# for the Luminus use case. In a real implementation, each agent might also:
#  - Integrate with an external API (CRM, usage data, billing info, etc.)
#  - Have specialized actions (e.g. "QUERY_LANGFLOW", "GET_CUSTOMER_USAGE", "SEND_BILLING_INFO", etc.)
#  - Use deeper conversation state tracking
#  - Enforce security and data privacy checks
