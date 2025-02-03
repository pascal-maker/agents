from agentarium import Agent

# Import the predefined agents
from agents.testbillingagent import testbilling_agent as testBillingAgent
from agents.testusageagent import testusage_agent as testUsageAgent
from agents.testadviceagent import testadvice_agent as testAdviceAgent

# Step 1: BillingAgent receives a customer inquiry
customer_query = "Waarom zijn mijn voorschotten verhoogd, terwijl ik geld terugkrijg?"
testBillingAgent.talk_to(testUsageAgent, customer_query)

# Step 2: UsageAgent provides usage insights and informs BillingAgent
usage_response = testUsageAgent.execute_action("EXPLAIN_USAGE", customer_query)
testUsageAgent.talk_to(testBillingAgent, usage_response)

# Step 3: BillingAgent processes the explanation and provides a billing response
testBillingAgent_response = testBillingAgent.execute_action("PROVIDE_BILLING_EXPLANATION", customer_query)

testBillingAgent.talk_to(testAdviceAgent, "Kun je energieadvies geven aan deze klant?")

# Step 4: AdviceAgent provides energy-saving tips
advice_response = testAdviceAgent.execute_action("PROVIDE_ENERGY_ADVICE", "Hoe kan ik energie besparen?")
testAdviceAgent.talk_to(testBillingAgent, advice_response)

# Print the final responses
print("\n--- Final Responses ---")
print("BillingAgent says:", testBillingAgent_response)
print("UsageAgent says:", usage_response)
print("AdviceAgent says:", advice_response)

# Display conversation logs
print("\n--- BillingAgent Interactions ---")
print(testBillingAgent.get_interactions())

print("\n--- UsageAgent Interactions ---")
print(testUsageAgent.get_interactions())

print("\n--- AdviceAgent Interactions ---")
print(testAdviceAgent.get_interactions())
