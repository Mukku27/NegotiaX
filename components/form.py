import streamlit as st

def negotiation_form():
    """Display the negotiation input form and return the collected values."""
    with st.form(key="negotiation_form"):
        col1, col2 = st.columns(2)
        with col1:
            your_offer = st.text_input(
                "Your Offer (₹ or %):", 
                placeholder="Enter your proposed offer...", 
                help="Enter your initial offer. Use ₹ for rupees or % for percentage."
            )
        with col2:
            other_party_stance = st.text_input(
                "Other Party's Expected Offer (₹ or %):", 
                placeholder="Enter expected counteroffer...", 
                help="Enter your estimate of the other party's initial offer. Use ₹ for rupees or % for percentage."
            )
        key_constraints = st.text_area(
            "Key Constraints", 
            height=150, 
            placeholder="List deal-breakers, goals, must-haves...", 
            help="List any important constraints, deal-breakers, or goals. Be as specific as possible."
        )
        scenario = st.text_area(
            "Scenario Details", 
            height=150, 
            placeholder="Describe the specific scenario (optional)", 
            help="Provide additional context for the negotiation."
        )
        submit_button = st.form_submit_button("Generate AI Strategy")
    return your_offer, other_party_stance, key_constraints, scenario, submit_button
