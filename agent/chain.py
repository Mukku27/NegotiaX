from agent.prompt import create_prompt
from agent.llm import load_LLM

def generate_strategy(groq_api_key, negotiation_type, your_offer, other_party_stance, key_constraints, scenario, history_text):
    """Generate an AI negotiation strategy given the inputs and conversation history."""
    llm = load_LLM(groq_api_key)
    prompt = create_prompt()
    chain = prompt | llm
    result = chain.invoke({
        "negotiation_type": negotiation_type,
        "your_offer": your_offer,
        "other_party_stance": other_party_stance,
        "key_constraints": key_constraints,
        "scenario": scenario,
        "history": history_text
    })
    result_content = result.content if hasattr(result, 'content') else str(result)
    return result_content
