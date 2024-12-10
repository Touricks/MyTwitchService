# utils.py
import streamlit as st
import base64
import os

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