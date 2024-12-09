# streamlit_app.py
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Twitch Content Recommendation System",
    page_icon="🎮",
    layout="wide"
)

# Hide default menu
hide_menu = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_menu, unsafe_allow_html=True)

# Custom navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "",  # Empty string removes the label above the radio buttons
    ["Project Overview", "System Demo", "Code Walkthrough"]
)

# Import your page functions
from pages.Project_Overview import project_overview
from pages.System_Demo import system_demo
from pages.Code_Walkthrough import code_walkthrough

# Display selected page content
if page == "Project Overview":
    project_overview()
elif page == "System Demo":
    system_demo()
elif page == "Code Walkthrough":
    code_walkthrough()