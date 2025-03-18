from langchain_groq import ChatGroq

def load_LLM(groq_api_key):
    """Loads the ChatGroq model for processing."""
    llm = ChatGroq(groq_api_key=groq_api_key, model_name="deepseek-r1-distill-llama-70b", streaming=True)
    return llm
