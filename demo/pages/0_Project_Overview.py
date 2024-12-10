import streamlit as st
import os
import base64

def set_background(image_file):
    """
    Sets a background image with reduced contrast and no white overlay.
    """
    with open(image_file, "rb") as f:
        img_data = f.read()

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
        pointer-events: none;
        filter: contrast(90%) brightness(90%);  
        opacity: 0.8;  
        z-index: -1;
    }}
    
    .stMarkdown {{
        color: black;
        background-color: rgba(255, 255, 255, 0.7);
        padding: 20px;
        border-radius: 10px;
        position: relative;
        z-index: 1;
        font-size: 16px;
    }}
    
    .stsubheader{{
        color: black;
        background-color: rgba(255, 255, 255, 0.7);
        padding: 20px;
        border-radius: 10px;
        position: relative;
        z-index: 1;
        font-size: 24px;
    }}
    
    .sttitle{{
        color: black;
        background-color: rgba(255, 255, 255, 0.7);
        padding: 20px;
        border-radius: 10px;
        position: relative;
        z-index: 1;
        font-size: 32px;
    }}
    
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)


st.title("🎮 Twitch Content Recommendation System")
set_background("demo/asset/background_picture.png")

# Rest of your code remains the same...
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

st.subheader("System Architecture")
st.image("demo/asset/System_Architecture.png", caption="System Architecture Diagram")

st.subheader("Technology Stack")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("**Frontend**")
    st.markdown("- React ")

with col2:
    st.markdown("**Backend**")
    st.markdown("- Spring Boot\n- MySQL\n- Twitch API")

with col3:
    st.markdown("**Deployment**")
    st.markdown("- AWS EC2\n- Docker\n - AppRunner")