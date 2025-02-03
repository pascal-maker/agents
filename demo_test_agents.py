"""
demo_test_agents.py

Demonstration of three improved Luminus Agents for Billing, Usage, and Advice,
renamed as testBillingAgent, testUsageAgent, and testAdviceAgent respectively,
based on the Agentarium framework.
"""

from agents.testbillingagent import testbilling_agent as testBillingAgent
from agents.testusageagent import testusage_agent as testUsageAgent
from agents.testadviceagent import testadvice_agent as testAdviceAgent

# 1) testBillingAgent asks testUsageAgent about usage data for a customer whose bill has increased
testBillingAgent.talk_to(
    testUsageAgent,
    "We have a customer asking: 'Waarom zijn mijn voorschotten verhoogd, terwijl ik toch geld terugkrijg?'"
)
testUsageAgent.talk_to(
    testBillingAgent,
    "Based on the usage logs, there's an increased peak in the evening. Also prices on the market went up."
)

# 2) testUsageAgent might pass some usage data to testAdviceAgent for tips
testUsageAgent.talk_to(
    testAdviceAgent,
    "The customer might want to reduce their evening usage. Could you provide some relevant tips?"
)

# 3) Each agent acts on its context
testBillingAgent.act()
testUsageAgent.act()
testAdviceAgent.act()

# 4) Let testBillingAgent provide an explanation via its custom action
response_billing = testBillingAgent.execute_action(
    "PROVIDE_BILLING_EXPLANATION",
    "Waarom zijn mijn voorschotten verhoogd, terwijl ik toch geld terugkrijg?"
)
print("BillingAgent says:", response_billing)

# 5) Let testUsageAgent provide usage insights
response_usage = testUsageAgent.execute_action(
    "EXPLAIN_USAGE",
    "Hoe kan ik mijn piekverbruik beter spreiden?"
)
print("UsageAgent says:", response_usage)

# 6) Let testAdviceAgent provide general energy savings
response_advice = testAdviceAgent.execute_action(
    "PROVIDE_ENERGY_ADVICE",
    "Hoe kan ik energie besparen?"
)
print("AdviceAgent says:", response_advice)

# 7) Show each agent's conversation log
print("\n--- BillingAgent Interactions ---")
print(testBillingAgent.get_interactions())

print("\n--- UsageAgent Interactions ---")
print(testUsageAgent.get_interactions())

print("\n--- AdviceAgent Interactions ---")
print(testAdviceAgent.get_interactions())