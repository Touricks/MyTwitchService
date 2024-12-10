import streamlit as st
import os
import base64

def set_background(image_file):
    """
    Sets a background image with unified text styles.
    """
    try:
        with open(image_file, "rb") as f:
            img_data = f.read()

        file_extension = os.path.splitext(image_file)[1][1:]
        bin_str = base64.b64encode(img_data).decode()

        page_bg_img = f'''
        <style>
        /* Remove default white background */
        .stApp {{
            background: none;
        }}
        
        /* Add background image */
        .stApp::before {{
            content: "";
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: url("data:image/{file_extension};base64,{bin_str}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            filter: contrast(90%) brightness(90%);
            opacity: 0.8;
            z-index: -1;
        }}
        
        /* Remove all default white backgrounds */
        header, .stDeployButton, section[data-testid="stSidebar"],
        .css-1dp5vir, .css-18ni7ap, .css-1d391kg {{
            background: none !important;
        }}
        
        /* Style for all text containers */
        .stMarkdown, .css-10trblm, .css-183lzff, .css-1vbkxwb,
        .stHeading, .css-qrbaxs {{
            color: black;
            background: none !important;
        }}
        
        /* Style for markdown content that needs white background */
        .stMarkdown > div > p,
        .stMarkdown > div > ul,
        .stMarkdown > div > h2,
        .stMarkdown > div > h3 {{
            background-color: rgba(255, 255, 255, 0.7);
            padding: 10px;
            border-radius: 5px;
            margin: 5px 0;
        }}

        /* Special style for headings */
        h1, h2, h3, .css-10trblm, .stHeading {{
            background-color: rgba(255, 255, 255, 0.7) !important;
            padding: 10px !important;
            border-radius: 5px !important;
            margin: 10px 0 !important;
        }}

        /* Style for lists */
        .element-container {{
            background: none !important;
        }}
        
        .element-container div {{
            background-color: rgba(255, 255, 255, 0.7) !important;
            padding: 10px;
            border-radius: 5px;
            margin: 5px 0;
        }}
        </style>
        '''
        st.markdown(page_bg_img, unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Error loading background image: {str(e)}")

# Hide streamlit default menu and footer
hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

# Use markdown for consistent styling
st.title("🎮 Twitch Content Recommendation System")
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

st.markdown("## System Architecture")
st.image("demo/asset/System_Architecture.png", caption="System Architecture Diagram")

st.markdown("## Technology Stack")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    **Frontend**
    - React
    """)

with col2:
    st.markdown("""
    **Backend**
    - Spring Boot
    - MySQL
    - Twitch API
    """)

with col3:
    st.markdown("""
    **Deployment**
    - AWS EC2
    - Docker
    """)