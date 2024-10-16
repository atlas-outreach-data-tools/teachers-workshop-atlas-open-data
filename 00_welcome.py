import streamlit as st
from utils import load_markdown_file_with_images, get_first_level_headers, load_markdown_preview

def run(selected_tab=None):
    folder = "welcome"

    # Initialize session state for expanded state of sections
    if "expanded_intro" not in st.session_state:
        st.session_state["expanded_intro"] = False
    if "expanded_standard_model" not in st.session_state:
        st.session_state["expanded_standard_model"] = False

    # Get the selected language from session state
    selected_language = st.session_state.get("language", "english").lower()

    tabs_path = ['01_welcome.md', '02_standard_model.md']

    # Show full content
    load_markdown_file_with_images(tabs_path[0], folder, selected_language)

    