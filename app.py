import streamlit as st
from agentarium import Agent, Action

# -----------------------------------------------------
# Hulpfuncties: Profaniteitsfilter en FAQ-detectie
# -----------------------------------------------------
def contains_profanity(text: str) -> bool:
    """
    Controleer of de tekst ongepaste (profane) woorden bevat.
    Dit is een vereenvoudigde lijst; pas deze gerust aan.
    """
    profane_words = ["shit", "fuck", "verdomme", "godverdomme", "kanker", "tyfus"]
    text_lower = text.lower()
    return any(word in text_lower for word in profane_words)

def is_faq_query(query: str) -> bool:
    """
    Bepaal of de vraag waarschijnlijk een FAQ betreft (op basis van sleutelwoorden).
    """
    keywords = ["grafiek", "voorschot", "factuur", "meterstand", "betalingen", "aanpassen"]
    query_lower = query.lower()
    return any(keyword in query_lower for keyword in keywords)

# -----------------------------------------------------
# Agents en acties definiëren
# -----------------------------------------------------

# --- AdviceAgent: Advies over energiebesparing ---
def provide_energy_advice(query: str, **kwargs) -> str:
    advice = [
        "Schakel elektrische toestellen volledig uit i.p.v. op stand-by.",
        "Overweeg om piekverbruik te spreiden buiten de drukke uren.",
        "Controleer isolatie en denk aan zonnepanelen of een warmtepomp.",
        "Monitor je verbruik via My Luminus om beter inzicht te krijgen."
    ]
    joined_advice = "\n• ".join(advice)
    return f"Hier zijn enkele algemene tips om energie te besparen:\n• {joined_advice}"

advice_agent = Agent.create_agent(name="AdviceAgent", occupation="Energy Advisor")
advice_agent.add_action(
    Action(
        name="PROVIDE_ENERGY_ADVICE",
        description="Geef tips voor het verlagen van energieverbruik en kostenbesparing",
        parameters=["query"],
        function=provide_energy_advice,
    )
)

# --- BillingAgent: Uitleg over facturatie en voorschotten ---
def provide_billing_explanation(query: str, **kwargs) -> str:
    if "voorschot" in query.lower():
        return (
            "Bij de berekening van je nieuwe voorschotten houden we rekening met "
            "gegevens zoals verwacht verbruik (bijv. normale winter, groothandelsprijzen, etc.).\n"
            "Zelfs als je geld terugkrijgt, kan het zijn dat de voorschotten omhooggaan "
            "als er een hogere verwachting is voor volgend jaar. "
            "Je kunt je voorschotbedrag zelf aanpassen in My Luminus, mits de voorwaarden zijn voldaan."
        )
    else:
        return (
            "Ik zie dat je een vraag hebt over je factuur of voorschotten. "
            "Kun je iets meer toelichten zodat ik je gerichter kan helpen? "
            "Je kunt ook My Luminus raadplegen voor directe aanpassingen."
        )

billing_agent = Agent.create_agent(name="BillingAgent", occupation="Billing Specialist")
billing_agent.add_action(
    Action(
        name="PROVIDE_BILLING_EXPLANATION",
        description="Geef uitleg over facturen en voorschotten",
        parameters=["query"],
        function=provide_billing_explanation,
    )
)

# --- UsageAgent: Uitleg over energieverbruik en grafieken ---
def explain_usage(query: str, **kwargs) -> str:
    return (
        "Op basis van je historische data geven we je verbruik weer in een grafiek. "
        "Als je geen grafiek ziet, kan dat komen doordat:\n"
        "• Je netbeheerder geen meterstanden heeft doorgegeven (bijvoorbeeld bij een meterwissel of nieuwe aansluiting).\n"
        "• Er meerdere tellers van hetzelfde type op dezelfde meter zijn geïnstalleerd.\n\n"
        "Controleer je MyLuminus App voor de laatste informatie of neem contact met ons op."
    )

usage_agent = Agent.create_agent(name="UsageAgent", occupation="Energy Usage Analyst")
usage_agent.add_action(
    Action(
        name="EXPLAIN_USAGE",
        description="Geef uitleg over verbruiksgegevens en grafiekweergave",
        parameters=["query"],
        function=explain_usage,
    )
)

# --- FAQAgent: Beantwoord veelgestelde vragen op basis van geïntegreerde informatie ---
def answer_faq(query: str, **kwargs) -> str:
    query_lower = query.lower()
    # Antwoord voor grafiekweergave van verbruik
    if "grafiek" in query_lower or ("verbruik" in query_lower and "weergave" in query_lower):
        return (
            "Jouw verbruik wordt weergegeven in een grafiek op basis van gegevens van je netbeheerder, "
            "aangevuld met je ingegeven meterstanden. Als je geen grafiek ziet, kan dat komen doordat:\n"
            "• Je netbeheerder geen meterstanden heeft doorgegeven (bijvoorbeeld bij een meterwissel of nieuwe aansluiting).\n"
            "• Er meerdere tellers van hetzelfde type op dezelfde meter zijn geïnstalleerd."
        )
    # Antwoord voor voorschotbedragen aanpassen
    elif "voorschot" in query_lower and "aanpassen" in query_lower:
        return (
            "Het aanpassen van je voorschotbedrag kan online niet als:\n"
            "• Je het al meerdere keren in deze facturatieperiode hebt gewijzigd.\n"
            "• De wijziging niet in lijn ligt met het volgende afrekenbedrag.\n"
            "• Je volgende factuur een afrekening is.\n"
            "• Je contract binnenkort niet meer actief is.\n"
            "• Er een openstaand saldo is (dat eerst betaald moet worden).\n"
            "• De verbruiksperiode korter is dan 3 maanden om een correcte berekening te maken.\n\n"
            "Neem anders contact met ons op; wij passen het bedrag graag voor je aan."
        )
    # Antwoord voor meer/minder voorschot betalen
    elif "meer of minder voorschot" in query_lower:
        return (
            "Om je voorschot aan te passen, meld je aan via My Luminus, ga naar 'Voorschot en afrekening' "
            "en klik op 'Wijzig voorschot'. Pas vervolgens het bedrag aan en bekijk de impact op je afrekening."
        )
    # Antwoord voor facturen en betalingen bekijken
    elif "facturen" in query_lower and "betalingen" in query_lower:
        return (
            "Log in via My Luminus en klik op 'Facturen en betalingen'. "
            "Je krijgt een overzichtstabel van al je facturen en betalingen. "
            "De status van je betalingen wordt aangegeven met:\n"
            "• Groen: volledig betaald\n"
            "• Oranje: nog te betalen (maar vervaldatum niet verstreken)\n"
            "• Rood: vervaldatum overschreden."
        )
    # Default antwoord
    else:
        return (
            "Geen antwoord gevonden op je vraag? Kies één van de contactmogelijkheden:\n"
            "• Chat (beschikbaar zodra een medewerker beschikbaar is)\n"
            "• Bel ons tijdens de openingsuren (Ma.-vr.: 08u00 - 18u00)"
        )

faq_agent = Agent.create_agent(name="FAQAgent", occupation="FAQ Specialist")
faq_agent.add_action(
    Action(
        name="ANSWER_FAQ",
        description="Beantwoord veelgestelde vragen op basis van geïntegreerde FAQ-informatie",
        parameters=["query"],
        function=answer_faq,
    )
)

# -----------------------------------------------------
# Streamlit App: Welkomstscherm en gebruikersinteractie
# -----------------------------------------------------

st.set_page_config(page_title="Luminus Energy Assistant", layout="wide")

# Welkomstscherm: Vraag de naam van de gebruiker (éénmalig per sessie)
if "username" not in st.session_state:
    st.title("Welkom bij de Luminus Energy Assistant")
    username_input = st.text_input("Voer je naam in:")
    if st.button("Start"):
        if username_input.strip():
            st.session_state["username"] = username_input.strip()
            st.success(f"Welkom, {st.session_state['username']}!")
            # Controleer of experimental_rerun beschikbaar is
            if hasattr(st, "experimental_rerun"):
                st.experimental_rerun()
        else:
            st.error("Voer alstublieft een geldige naam in.")
    st.stop()
else:
    username = st.session_state["username"]
    st.sidebar.write(f"**Ingelogd als:** {username}")

st.header("Stel je vraag over energie, facturatie of besparing")
customer_query = st.text_area("Typ hier je vraag:")

if st.button("Verzend vraag"):
    if not customer_query.strip():
        st.error("Voer alstublieft een geldige vraag in.")
    elif contains_profanity(customer_query):
        st.error("Helaas, uw taalgebruik is niet toegestaan.")
    else:
        # Indien de vraag lijkt te vallen onder de FAQ (op basis van sleutelwoorden), roep dan FAQAgent aan
        if is_faq_query(customer_query):
            faq_response = faq_agent.execute_action("ANSWER_FAQ", customer_query)
            st.markdown("### Antwoord:")
            st.write(faq_response)
        else:
            # Anders: Voer de multi-agent conversatiestroom uit (Billing, Usage, Advice)
            # Stap 1: BillingAgent ontvangt de vraag en stuurt deze door naar UsageAgent
            billing_agent.talk_to(usage_agent, customer_query)

            # Stap 2: UsageAgent geeft inzicht in het gebruik (bijvoorbeeld over grafiekweergave)
            usage_response = usage_agent.execute_action("EXPLAIN_USAGE", customer_query)
            usage_agent.talk_to(billing_agent, usage_response)

            # Stap 3: BillingAgent verwerkt de vraag verder en geeft een facturatie-/voorschot-antwoord
            billing_response = billing_agent.execute_action("PROVIDE_BILLING_EXPLANATION", customer_query)

            # Stap 4: BillingAgent vraagt tevens energieadvies op bij AdviceAgent
            billing_agent.talk_to(advice_agent, "Kun je energieadvies geven aan deze klant?")
            advice_response = advice_agent.execute_action("PROVIDE_ENERGY_ADVICE", "Hoe kan ik energie besparen?")
            advice_agent.talk_to(billing_agent, advice_response)

            # Weergeven van de antwoorden van de verschillende agents
            st.markdown("### Antwoorden van onze experts:")
            st.markdown("**BillingAgent zegt:**")
            st.write(billing_response)

            st.markdown("**UsageAgent zegt:**")
            st.write(usage_response)

            st.markdown("**AdviceAgent zegt:**")
            st.write(advice_response)

        # (Optioneel) Toon conversatielogs van de agents
        with st.expander("Toon conversatielogs"):
            st.markdown("**BillingAgent Interacties:**")
            st.text(billing_agent.get_interactions())

            st.markdown("**UsageAgent Interacties:**")
            st.text(usage_agent.get_interactions())

            st.markdown("**AdviceAgent Interacties:**")
            st.text(advice_agent.get_interactions())

            st.markdown("**FAQAgent Interacties:**")
            st.text(faq_agent.get_interactions())
