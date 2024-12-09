import streamlit as st

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