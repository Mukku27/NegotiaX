import os
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    st.error("Groq API Key not found in .env file")
    st.stop()


st.set_page_config(page_title="AI Negotiation Agent", layout="wide")
st.title("🤝 AI-Powered Negotiation Agent")

st.sidebar.header("Negotiation Settings")
st.sidebar.markdown("Select your negotiation type and explore the details below.")
negotiation_type = st.sidebar.selectbox("Negotiation Type", [
    "Salary Negotiation",
    "Business Deal",
    "Freelance Pricing",
    "Contract Dispute"
])

with st.expander("How to use this app"):
    st.markdown("""
    - Fill in your offer, the opposing offer, and key constraints.
    - Click **Generate AI Strategy** to receive suggestions.
    - Use the sidebar to adjust the negotiation type.
    """)

negotiation_template = """
You are an expert negotiator. Analyze this scenario and suggest the best negotiation strategy:
- **Negotiation Type:** {negotiation_type}
- **Your Offer:** {your_offer}
- **Other Party's Expected Offer:** {other_party_stance}
- **Key Constraints:** {key_constraints}

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
        your_offer = st.text_input("Your Offer (₹ or %):", placeholder="Enter your proposed offer...")
    with col2:
        other_party_stance = st.text_input("Other Party's Expected Offer (₹ or %):", placeholder="Enter expected counteroffer...")
    key_constraints = st.text_area("Key Constraints", height=150, placeholder="List deal-breakers, goals, must-haves...")
    submit_button = st.form_submit_button("Generate AI Strategy")

if submit_button:
    if your_offer and other_party_stance and key_constraints:
        with st.spinner("Generating negotiation strategy..."):
            llm = load_LLM(groq_api_key)
            prompt = PromptTemplate(
                input_variables=["negotiation_type", "your_offer", "other_party_stance", "key_constraints"],
                template=negotiation_template
            )
            chain = prompt | llm
            
            result = chain.invoke({
                "negotiation_type": negotiation_type,
                "your_offer": your_offer,
                "other_party_stance": other_party_stance,
                "key_constraints": key_constraints
            })
            
            result_content = result.content if hasattr(result, 'content') else str(result)
            
            st.success("Strategy generated successfully!")
            st.subheader("💡 AI's Suggested Strategy:")
            st.markdown(result_content)
    else:
        st.error("Please fill in all fields before generating a strategy.")
