from langchain.prompts import PromptTemplate
prompt = PromptTemplate(
                    input_variables=["negotiation_type", "your_offer", "other_party_stance", "key_constraints", "scenario", "history"],
                    template="""
                    You are an expert negotiator. Analyze this scenario and suggest the best negotiation strategy.
                    - **Negotiation Type:** {negotiation_type}
                    - **Your Offer:** {your_offer}
                    - **Other Party's Expected Offer:** {other_party_stance}
                    - **Key Constraints:** {key_constraints}
                    - **Scenario:** {scenario}
                    - **Previous History:** {history}
                    """
                )
                