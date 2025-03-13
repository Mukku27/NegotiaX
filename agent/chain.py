from agent.prompt import prompt
from agent.llm import load_LLM
from main import groq_api_key
llm = load_LLM(groq_api_key)
chain = prompt | llm