import streamlit as st
import base64

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover;
        background-repeat: no-repeat;
    }}
    </style>
    """,
        unsafe_allow_html=True
    )

st.set_page_config(
    page_title="Video Recommendation System",
    page_icon="🎮",
    layout="wide"
)
# Use it in your app
add_bg_from_local('demo/asset/background_picture.png')
# Main page content
st.title("Personalized Video Recommendation System")
# Demo Video
st.subheader("Please Watch the Demo video")
st.video("path_to_demo_video.mp4")