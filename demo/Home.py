import streamlit as st
from utils.image_utils import adjust_contrast

# Set page config
st.set_page_config(
    page_title="Personalized Video Recommendation System",
    page_icon="🎮",
    layout="wide"
)

# Main page content
st.title("Personalized Video Recommendation System Proposal")
# Demo Video
st.subheader("Please Watch the Demo video")
st.video("path_to_demo_video.mp4")

# Process and display background
background_image_path = "background.JPG"
contrast_factor = 0.3
adjusted_image = adjust_contrast(background_image_path, contrast_factor)