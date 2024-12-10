import streamlit as st
from utils.utils import set_background
st.set_page_config(
    page_title="Video Recommendation System",
    page_icon="🎮",
    layout="wide"
)

st.title("Personalized Video Recommendation System")
set_background("demo/asset/background_picture.png")
# Demo Video
st.subheader("Please Watch the Demo video")
st.video("path_to_demo_video.mp4")