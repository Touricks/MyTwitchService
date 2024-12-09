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
    page = st.sidebar.radio(
        "Select a Page",
        ["Project Overview", "System Demo", "Code Walkthrough"]
    )

    if page == "Project Overview":
        show_project_overview()
    elif page == "System Demo":
        show_system_demo()
    elif page == "Code Walkthrough":
        show_code_walkthrough()

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

    # Architecture Image
    st.subheader("System Architecture")
    st.image("path_to_architecture_diagram.png", caption="System Architecture Diagram")

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

def show_system_demo():
    st.title("System Demo")

    # Demo Video
    st.subheader("Watch the Demo")
    st.video("path_to_demo_video.mp4")

    # Feature Screenshots
    st.subheader("Key Features in Action")

    # User Interface
    st.markdown("### User Interface")
    st.image("path_to_ui_screenshot.png", caption="Main User Interface")

    # Recommendation System
    st.markdown("### Recommendation System")
    st.image("path_to_recommendations_screenshot.png", caption="Game Recommendations")

    # Language Filtering
    st.markdown("### Language Filtering")
    st.image("path_to_language_screenshot.png", caption="Language Selection Interface")

def show_code_walkthrough():
    st.title("Code Walkthrough")

    # Backend Code Examples
    st.subheader("Backend Implementation")

    # Recommendation Service
    st.markdown("### Recommendation Service")
    recommendation_code = '''
    @Service
    public class RecommendationService {
        public List<Video> getVideos(String gameId, int first) {
            return twitchApiClient.getVideos(gameId, first).data().stream()
                    .filter(video -> DEFAULT_LANGUAGE.equals(video.language()))
                    .filter(video -> {
                        String thumbnailUrl = video.thumbnailUrl();
                        return thumbnailUrl != null 
                            && !thumbnailUrl.isEmpty()
                            && !thumbnailUrl.contains("404_processing");
                    })
                    .limit(first)
                    .collect(Collectors.toList());
        }
    }
    '''
    st.code(recommendation_code, language='java')

    # Frontend Code Examples
    st.subheader("Frontend Implementation")

    # React Component
    st.markdown("### Video Card Component")
    frontend_code = '''
    const VideoCard = ({ video }) => {
        const thumbnailUrl = processThumbnailUrl(video.thumbnail_url);
        
        return (
            <div className="video-card">
                {thumbnailUrl && !thumbnailUrl.includes('404') ? (
                    <img src={thumbnailUrl} alt={video.title} />
                ) : (
                    <div className="thumbnail-placeholder">
                        <span>{video.title}</span>
                    </div>
                )}
            </div>
        );
    };
    '''
    st.code(frontend_code, language='javascript')

if __name__ == "__main__":
    main()