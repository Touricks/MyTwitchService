import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from PIL import Image
import json

# Configure page settings
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
    # Sidebar
    st.sidebar.title("Navigation")
    page = st.sidebar.radio(
        "Select a Page",
        ["Project Overview", "Game Recommendations", "Stream Analysis", "User Statistics"]
    )

    if page == "Project Overview":
        show_project_overview()
    elif page == "Game Recommendations":
        show_game_recommendations()
    elif page == "Stream Analysis":
        show_stream_analysis()
    elif page == "User Statistics":
        show_user_statistics()

def show_project_overview():
    st.title("🎮 Twitch Content Recommendation System")

    # Project Description
    st.markdown("""
    ## About the Project
    This recommendation system helps users discover Twitch content based on their preferences.
    The system analyzes user behavior and provides personalized recommendations for games,
    streams, and videos.
    
    ### Key Features
    - Personalized game recommendations
    - Language-based content filtering
    - User preference tracking
    - Real-time Twitch data integration
    """)

    # Architecture Overview
    st.subheader("System Architecture")
    # You can add an architecture diagram here
    # st.image("architecture.png")

    # Technology Stack
    st.subheader("Technology Stack")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("**Frontend**")
        st.markdown("- React\n- Material UI\n- Axios")

    with col2:
        st.markdown("**Backend**")
        st.markdown("- Spring Boot\n- MySQL\n- Twitch API")

    with col3:
        st.markdown("**Deployment**")
        st.markdown("- AWS EC2\n- AWS RDS\n- Docker")

def show_game_recommendations():
    st.title("Game Recommendations")

    # Language Filter
    language = st.selectbox(
        "Select Language",
        ["en", "es", "fr", "de", "ja", "ko", "zh"]
    )

    # Mock data - replace with actual API call
    games_data = load_data(f"games?language={language}")

    if games_data:
        # Display games in a grid
        cols = st.columns(4)
        for idx, game in enumerate(games_data):
            with cols[idx % 4]:
                st.image(game.get('thumbnailUrl', 'placeholder.png'), use_column_width=True)
                st.write(game.get('title', 'Unknown Game'))
                st.write(f"👥 {game.get('viewerCount', 0)} viewers")

def show_stream_analysis():
    st.title("Stream Analysis")

    # Date range selector
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date")
    with col2:
        end_date = st.date_input("End Date")

    # Mock data - replace with actual API call
    stream_data = load_data(f"streams/analysis?start={start_date}&end={end_date}")

    if stream_data:
        # Create viewer distribution chart
        fig = px.bar(
            stream_data,
            x='timeSlot',
            y='viewerCount',
            title='Viewer Distribution Over Time'
        )
        st.plotly_chart(fig)

        # Display top streams
        st.subheader("Top Streams")
        df = pd.DataFrame(stream_data['topStreams'])
        st.dataframe(df)

def show_user_statistics():
    st.title("User Statistics")

    # Mock user stats - replace with actual API call
    user_stats = load_data("users/statistics")

    if user_stats:
        # Display key metrics
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric("Total Users", user_stats.get('totalUsers', 0))

        with col2:
            st.metric("Active Users", user_stats.get('activeUsers', 0))

        with col3:
            st.metric("Total Favorites", user_stats.get('totalFavorites', 0))

        with col4:
            st.metric("Active Sessions", user_stats.get('activeSessions', 0))

        # User engagement chart
        engagement_data = user_stats.get('engagementData', [])
        if engagement_data:
            fig = px.line(
                engagement_data,
                x='date',
                y='engagement',
                title='User Engagement Over Time'
            )
            st.plotly_chart(fig)

if __name__ == "__main__":
    main()