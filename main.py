import streamlit as st
from components.sidebar import sidebar
from components.ui_elements import show_instructions, show_conversation_history
from components.form import negotiation_form


def main():
    st.set_page_config(page_title="AI Negotiation Agent", layout="wide")
    st.title("🤝 AI-Powered Negotiation Agent")
    
    groq_api_key = st.text_input("Enter your Groq API key:", type="password")
    if not groq_api_key:
        st.error("Please enter your Groq API key.")
        st.stop()
    
    sidebar()
    show_instructions()
    show_conversation_history()
    negotiation_form()

if __name__ == "__main__":
    main()
