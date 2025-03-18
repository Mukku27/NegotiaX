import streamlit as st
from components.sidebar import render_sidebar
from components.ui_elements import show_instructions, show_conversation_history
from components.form import render_negotiation_form
from components.startup_page import startup_page

def main() -> None:
    startup_page()
    render_sidebar()
    show_instructions()
    show_conversation_history()
    render_negotiation_form()

if __name__ == "__main__":
    main()
