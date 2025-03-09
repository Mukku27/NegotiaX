import os
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    st.error("Groq API Key not found in .env file. Please check your .env file.")
    st.stop()

st.set_page_config(page_title="AI Negotiation Agent", layout="wide")
st.title("🤝 AI-Powered Negotiation Agent")

# Initialize conversation history in session state if not already set
if "conversation_history" not in st.session_state:
    st.session_state["conversation_history"] = []

# Sidebar: Negotiation settings and reset option
st.sidebar.header("Negotiation Settings")
st.sidebar.markdown("Select your negotiation type and explore the details below.")
negotiation_types = [
    "Salary Negotiation",
    "Business Deal",
    "Freelance Pricing",
    "Contract Dispute",
    "Real Estate Negotiation",
    "Merger and Acquisition Negotiation",
    "Dispute Resolution"
]
negotiation_type = st.sidebar.selectbox("Negotiation Type", negotiation_types)

if st.sidebar.button("Reset Conversation"):
    st.session_state["conversation_history"] = []
    st.success("Conversation history reset!")

with st.expander("How to use this app"):
    st.markdown("""
    1. **Select Negotiation Type:** Choose the type of negotiation from the sidebar.
    2. **Enter Your Offer:** Specify your initial offer (e.g., salary amount, price, etc.). Use ₹ for rupees or % for percentage.
    3. **Enter Other Party's Expected Offer:** Provide your estimate of the other party's initial offer. Use ₹ for rupees or % for percentage.
    4. **Key Constraints:** Detail any important constraints, deal-breakers, or goals. Be as specific as possible.
    5. **Generate AI Strategy:** Click the button to receive AI-generated negotiation strategies.
    6. **Multi-turn Simulation:** Previous turns will be preserved below for a history-aware dialogue.
    """)

# Display previous conversation history
st.subheader("🗨️ Negotiation History")
if st.session_state["conversation_history"]:
    for turn in st.session_state["conversation_history"]:
        st.markdown(f"**You:** {turn['user']}")
        st.markdown(f"**AI:** {turn['assistant']}")
else:
    st.info("No conversation history yet. Start your negotiation!")

# Updated negotiation template includes conversation history
negotiation_template = """
You are an expert negotiator. Analyze this scenario and suggest the best negotiation strategy based on the previous conversation.
- **Negotiation Type:** {negotiation_type}
- **Your Offer:** {your_offer}
- **Other Party's Expected Offer:** {other_party_stance}
- **Key Constraints:** {key_constraints}
- **Scenario:** {scenario}

### Previous Negotiation History:
{history}

### Provide:
1. The best counteroffer.
2. Justification with reasoning.
3. Risk assessment (if any).
4. Confidence score (out of 100%).
"""

def load_LLM(groq_api_key):
    """Loads the ChatGroq model for processing."""
    llm = ChatGroq(groq_api_key=groq_api_key, model_name="deepseek-r1-distill-llama-70b", streaming=True)
    return llm

st.header(f"💼 {negotiation_type}")
st.markdown("Enter details of your negotiation scenario below:")

with st.form(key="negotiation_form"):
    col1, col2 = st.columns(2)
    with col1:
        your_offer = st.text_input("Your Offer (₹ or %):", placeholder="Enter your proposed offer...", help="Enter your initial offer. Use ₹ for rupees or % for percentage.")
    with col2:
        other_party_stance = st.text_input("Other Party's Expected Offer (₹ or %):", placeholder="Enter expected counteroffer...", help="Enter your estimate of the other party's initial offer. Use ₹ for rupees or % for percentage.")
    key_constraints = st.text_area("Key Constraints", height=150, placeholder="List deal-breakers, goals, must-haves...", help="List any important constraints, deal-breakers, or goals. Be as specific as possible.")
    scenario = st.text_area("Scenario Details", height=150, placeholder="Describe the specific scenario (optional)", help="Provide additional context for the negotiation.")
    submit_button = st.form_submit_button("Generate AI Strategy")

if submit_button:
    if your_offer and other_party_stance and key_constraints:
        with st.spinner("Generating negotiation strategy..."):
            llm = load_LLM(groq_api_key)
            # Combine previous conversation history into a single string
            history_text = ""
            for turn in st.session_state["conversation_history"]:
                history_text += f"You: {turn['user']}\nAI: {turn['assistant']}\n"
            if not history_text:
                history_text = "None"
            
            # Create the prompt including conversation history
            prompt = PromptTemplate(
                input_variables=["negotiation_type", "your_offer", "other_party_stance", "key_constraints", "scenario", "history"],
                template=negotiation_template
            )
            chain = prompt | llm
            
            # Invoke the chain to generate AI strategy
            result = chain.invoke({
                "negotiation_type": negotiation_type,
                "your_offer": your_offer,
                "other_party_stance": other_party_stance,
                "key_constraints": key_constraints,
                "scenario": scenario,
                "history": history_text
            })
            
            result_content = result.content if hasattr(result, 'content') else str(result)
            
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
