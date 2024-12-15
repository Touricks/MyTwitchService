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
st.subheader("Click the button below to view the System in demo video")

st.markdown("[Entry](https://hsnim2dpva.us-east-1.awsapprunner.com )")

st.subheader("Demo video")
st.video("https://www.youtube.com/watch?v=_n-Tb5B5em4")