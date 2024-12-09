import streamlit as st
import requests
from PIL import Image
# Configure page settings
# noinspection PyInterpreter
st.set_page_config(
    page_title="Twitch Content Recommendation System",
    page_icon="🎮",
    layout="wide"
)

# Backend API URL
BACKEND_URL = "http://localhost:8080"  # Replace with your actual backend URL

def load_data(endpoint):
    try:
        response = requests.get(f"{BACKEND_URL}/{endpoint}")
        return response.json()
    except Exception as e:
        st.error(f"Error loading data: {str(e)}")
        return None

def main():
    # Sidebar navigation
    st.sidebar.title("Navigation")

if __name__ == "__main__":
    main()