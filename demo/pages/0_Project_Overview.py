import streamlit as st
import os
import base64

def set_background(image_file):
    """
    A function to unpack an image from root folder and set as bg.
    """
    try:
        with open(image_file, "rb") as f:
            img_data = f.read()

        # Get the file extension
        file_extension = os.path.splitext(image_file)[1][1:]

        bin_str = base64.b64encode(img_data).decode()

        page_bg_img = f'''
        <style>
        .stApp {{
            background-image: url("data:image/{file_extension};base64,{bin_str}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        
        .stApp::before {{
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(255, 255, 255, 0.3);
            pointer-events: none;
        }}
        
        .stMarkdown {{
            color: black;
            background-color: rgba(255, 255, 255, 0.7);
            padding: 20px;
            border-radius: 10px;
        }}
        </style>
        '''
        st.markdown(page_bg_img, unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Error loading background image: {str(e)}")

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