import streamlit as st
from components.sidebar import negotiation_sidebar, api_key_sidebar
from components.form import negotiation_form
from components.ui_elements import display_conversation_history, display_app_instructions
from agent.chain import generate_strategy

st.set_page_config(page_title="AI Negotiation Agent", layout="wide")
st.title("🤝 AI-Powered Negotiation Agent")

# Display API key instructions and input field
api_key_sidebar()
groq_api_key = st.text_input("Enter your Groq API key:", type="password")
if not groq_api_key:
    st.error("Please enter your Groq API key.")
    st.stop()

# Initialize conversation history in session state if not already set
if "conversation_history" not in st.session_state:
    st.session_state["conversation_history"] = []

# Sidebar: Negotiation settings
negotiation_types = [
    "Salary Negotiation",
    "Business Deal",
    "Freelance Pricing",
    "Contract Dispute",
    "Real Estate Negotiation",
    "Merger and Acquisition Negotiation",
    "Dispute Resolution"
]
negotiation_type = negotiation_sidebar(negotiation_types)

# Display app instructions and conversation history
display_app_instructions()
display_conversation_history()

st.header(f"💼 {negotiation_type}")
st.markdown("Enter details of your negotiation scenario below:")

your_offer, other_party_stance, key_constraints, scenario, submit_button = negotiation_form()

if submit_button:
    if your_offer and other_party_stance and key_constraints:
        with st.spinner("Generating negotiation strategy..."):
            # Combine previous conversation history into a single string
            history_text = ""
            for turn in st.session_state["conversation_history"]:
                history_text += f"You: {turn['user']}\nAI: {turn['assistant']}\n"
            if not history_text:
                history_text = "None"

            # Generate AI strategy using the chain from the agent module
            result_content = generate_strategy(
                groq_api_key,
                negotiation_type,
                your_offer,
                other_party_stance,
                key_constraints,
                scenario,
                history_text
            )

            st.success("Strategy generated successfully!")
            st.subheader("💡 AI's Suggested Strategy:")
            st.markdown(result_content)

            # Append the new turn to the conversation history
            st.session_state["conversation_history"].append({
                "user": f"Offer: {your_offer}, Expected: {other_party_stance}, Constraints: {key_constraints}, Scenario: {scenario}",
                "assistant": result_content
            })
    else:
        st.error("Please fill in all required fields before generating a strategy.")
