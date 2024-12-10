import streamlit as st
from ..utils import set_background

st.title("🎮 Twitch Content Recommendation System")
# Project Description
set_background("demo/asset/background_picture.png")
st.markdown("""
    ## About the Project
    This recommendation system helps users discover Twitch content based on their preferences.
    The system analyzes user behavior and provides personalized recommendations for games,
    streams, and videos.
    
    ### Key Features
    - Personalized game recommendations
    - User preference tracking
    - Real-time Twitch data integration
    """)
# Architecture Image
st.subheader("System Architecture")
st.image("demo/asset/System_Architecture.png", caption="System Architecture Diagram")

# Technology Stack
st.subheader("Technology Stack")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Frontend**")
    st.markdown("- React - ")

with col2:
    st.markdown("**Backend**")
    st.markdown("- Spring Boot\n- MySQL\n- Twitch API")

with col3:
    st.markdown("**Deployment**")
    st.markdown("- AWS EC2\n- Docker\n")