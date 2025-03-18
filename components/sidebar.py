import streamlit as st

def negotiation_sidebar(negotiation_types):
    """Display the negotiation settings sidebar and return the selected negotiation type."""
    st.sidebar.header("Negotiation Settings")
    st.sidebar.markdown("Select your negotiation type and explore the details below.")
    negotiation_type = st.sidebar.selectbox("Negotiation Type", negotiation_types)
    if st.sidebar.button("Reset Conversation"):
        st.session_state["conversation_history"] = []
        st.sidebar.success("Conversation history reset!")
    return negotiation_type

def api_key_sidebar():
    """Display instructions for obtaining a Groq API key in the main area."""
    st.markdown("""
    To use this app, you'll need a Groq API key. Don't worry, it's free! Here's how to get one:
    
    1. **Go to:** [https://console.groq.com](https://console.groq.com)
    2. **Sign up:** Create a free account (you'll need an email). You'll get a verification email; click the link inside.
    3. **Log in:** Use your new account details.
    4. **Find API Keys:** Look for "API Keys" in the left-hand menu.
    5. **Create a key:** Click "Create API Key", give it a name (like "MyNegotiationKey"), and submit.
    6. **Keep it safe!:** Copy your key immediately – you won't see it again! Store it securely.
    """)
