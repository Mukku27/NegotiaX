import streamlit as st

def display_conversation_history():
    """Display the previous negotiation conversation history."""
    st.subheader("🗨️ Negotiation History")
    if st.session_state.get("conversation_history"):
        for turn in st.session_state["conversation_history"]:
            st.markdown(f"**You:** {turn['user']}")
            st.markdown(f"**AI:** {turn['assistant']}")
    else:
        st.info("No conversation history yet. Start your negotiation!")

def display_app_instructions():
    """Display instructions on how to use the app."""
    with st.expander("How to use this app"):
        st.markdown("""
        1. **Select Negotiation Type:** Choose the type of negotiation from the sidebar.
        2. **Enter Your Offer:** Specify your initial offer (e.g., salary amount, price, etc.). Use ₹ for rupees or % for percentage.
        3. **Enter Other Party's Expected Offer:** Provide your estimate of the other party's initial offer. Use ₹ for rupees or % for percentage.
        4. **Key Constraints:** Detail any important constraints, deal-breakers, or goals. Be as specific as possible.
        5. **Generate AI Strategy:** Click the button to receive AI-generated negotiation strategies.
        6. **Multi-turn Simulation:** Previous turns will be preserved below for a history-aware dialogue.
        """)
