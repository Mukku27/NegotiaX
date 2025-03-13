import streamlit as st

def sidebar():
    st.sidebar.header("Negotiation Settings")
    negotiation_types = [
        "Salary Negotiation",
        "Business Deal", 
        "Freelance Pricing",
        "Contract Dispute",
        "Real Estate Negotiation", 
        "Merger and Acquisition Negotiation",
        "Dispute Resolution"
    ]
    
    st.sidebar.selectbox("Negotiation Type", negotiation_types, key="negotiation_type")
    
    if st.sidebar.button("Reset Conversation"):

        st.session_state["conversation_history"] = []
        st.success("Conversation history reset!")