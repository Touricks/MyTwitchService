import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Twitch Content Recommendation System",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# More specific CSS to hide streamlit app and customize navigation
st.markdown("""
    <style>
        [data-testid="collapsedControl"] {
            display: none
        }
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        /* Hide Streamlit app text */
        div[data-testid="stSidebarNav"] > ul {
            padding-top: 0rem;
        }
        div[data-testid="stSidebarNav"] > ul > li:first-child {
            display: none;
        }
        /* Custom navigation header */
        div[data-testid="stSidebarNav"]:before {
            content: "Navigation";
            margin-left: 20px;
            margin-top: 20px;
            font-size: 24px;
            position: relative;
            top: 0;
        }
        /* Reduce space at top of sidebar */
        section[data-testid="stSidebar"] > div {
            padding-top: 1rem;
        }
    </style>
""", unsafe_allow_html=True)

# Auto-redirect to Project Overview
import time
time.sleep(0.1)  # Small delay to ensure smooth transition
st.switch_page("pages/0_Project_Overview.py")