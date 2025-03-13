from setuptools import setup, find_packages

setup(
    name="ai_negotiation_agent",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "streamlit",
        "langchain",
        "langchain_groq"
    ]
)