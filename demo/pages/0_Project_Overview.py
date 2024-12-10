import streamlit as st
import os
import base64

def set_background(image_file):
    """
    Sets a background image for the Streamlit app with a semi-transparent overlay.

    Args:
        image_file (str): Path to the background image file
    """
    try:
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
            background: rgba(255, 255, 255, 0.3);
            pointer-events: none;
        }}
        
        .stMarkdown {{
            color: black;
            background-color: rgba(255, 255, 255, 0.7);
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 1rem;
        }}

        /* Fixed header styling */
        .css-18e3th9 {{
            padding-top: 0;
        }}

        .css-1d391kg {{
            padding-top: 3.5rem;
        }}

        h1 {{
            background-color: rgba(255, 255, 255, 0.7);
            padding: 1rem;
            border-radius: 10px;
            margin-top: 0;
            position: relative;
        }}

        .tech-card {{
            background-color: rgba(255, 255, 255, 0.9);
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            height: 100%;
        }}
        
        .section-header {{
            background-color: rgba(145, 70, 255, 0.1);
            padding: 10px;
            border-radius: 5px;
            margin-bottom: 15px;
        }}
        </style>
        '''
        st.markdown(page_bg_img, unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Error loading background image: {str(e)}")

def main():
    st.set_page_config(
        page_title="Twitch Content Recommendation System",
        page_icon="🎮",
        layout="wide"
    )

    set_background("demo/asset/background_picture.png")

    # Header Section with improved alignment
    st.title("🎮 Twitch Content Recommendation System")

    # About Section
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

    # Rest of the code remains the same...
    # (Previous implementation of architecture section, technology stack, etc.)

if __name__ == "__main__":
    main()