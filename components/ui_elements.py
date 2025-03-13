import streamlit as st

def show_instructions():
    with st.expander("How to use this app"):
        st.markdown("""
        1. **Select Negotiation Type**
        2. **Enter Your Offer**
        3. **Enter Other Party's Expected Offer**
        4. **Key Constraints**
        5. **Generate AI Strategy**
        6. **Multi-turn Simulation**
        """)

def show_conversation_history():
    st.subheader("🗨️ Negotiation History")
    if "conversation_history" not in st.session_state:
        st.session_state["conversation_history"] = []
    
    if st.session_state["conversation_history"]:
        for turn in st.session_state["conversation_history"]:
            st.markdown(f"**You:** {turn['user']}")
            st.markdown(f"**AI:** {turn['assistant']}")
    else:
        st.info("No conversation history yet. Start your negotiation!")