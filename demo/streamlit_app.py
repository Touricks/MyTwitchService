import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Twitch Content Recommendation System",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
        header[data-testid="stSidebarHeader"] {
            display: none;
        }
        [data-testid="stSidebarNav"] {
            background-image: none;
            padding-top: 1.5rem;
        }
        [data-testid="stSidebarNav"]::before {
            content: "Navigation";
            margin-left: 20px;
            margin-top: 20px;
            font-size: 24px;
            position: relative;
            top: 0;
        }
    </style>
""", unsafe_allow_html=True)

# Auto-redirect to Project Overview
import time
time.sleep(0.1)  # Small delay to ensure smooth transition
st.switch_page("pages/Project_Overview.py")