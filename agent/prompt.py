from langchain.prompts import PromptTemplate

negotiation_template = """
You are an expert negotiator. Analyze this scenario and suggest the best negotiation strategy based on the previous conversation.
- **Negotiation Type:** {negotiation_type}
- **Your Offer:** {your_offer}
- **Other Party's Expected Offer:** {other_party_stance}
- **Key Constraints:** {key_constraints}
- **Scenario:** {scenario}

### Previous Negotiation History:
{history}

### Provide:
1. The best counteroffer.
2. Justification with reasoning.
3. Risk assessment (if any).
4. Confidence score (out of 100%).
"""

def create_prompt():
    return PromptTemplate(
        input_variables=["negotiation_type", "your_offer", "other_party_stance", "key_constraints", "scenario", "history"],
        template=negotiation_template
    )
