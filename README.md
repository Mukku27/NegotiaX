# NegotiaX

**AI-Powered Negotiation Agent**

This project provides an AI-driven negotiation assistant built with Streamlit and LangChain. It supports multi-turn conversation with history-awareness for enhanced negotiation simulations.

## Features

- **Negotiation Types:** Salary, Business Deals, Freelance Pricing, Contract Dispute, Real Estate Negotiation, Merger and Acquisition Negotiation, and Dispute Resolution.
- **Multi-turn Simulation:** Maintains previous negotiation turns to provide history-aware dialogue.
- **AI Strategy Generation:** Leverages a Groq-backed language model to suggest optimal negotiation strategies.

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/negotiaX.git
   cd negotiaX
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app:**
   ```bash
   streamlit run main.py
   ```

4. **Groq API Key:**  
   Follow the instructions provided in the app to obtain your free Groq API key and enter it when prompted.

## Project Structure

```
negotiaX/
├── agent/
│   ├── __init__.py
│   ├── chain.py
│   ├── llm.py
│   └── prompt.py
├── components/
│   ├── __init__.py
│   ├── form.py
│   ├── sidebar.py
│   └── ui_elements.py
├── main.py
├── setup.py
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## License

This project is licensed under the MIT License.
```