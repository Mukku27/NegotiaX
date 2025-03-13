from langchain_groq import ChatGroq

def load_LLM(groq_api_key):
    return ChatGroq(groq_api_key=groq_api_key, model_name="deepseek-r1-distill-llama-70b", streaming=True)