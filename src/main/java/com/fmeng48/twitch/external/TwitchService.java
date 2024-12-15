package com.fmeng48.twitch.external;


import com.fmeng48.twitch.external.model.Game;
import com.fmeng48.twitch.external.model.Stream;
import com.fmeng48.twitch.external.model.Video;
import com.fmeng48.twitch.external.model.Clip;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.stereotype.Service;


import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;


@Service
public class TwitchService {


    private final TwitchApiClient twitchApiClient;
    private static final String DEFAULT_LANGUAGE = "en";

    public TwitchService(TwitchApiClient twitchApiClient) {
        this.twitchApiClient = twitchApiClient;
    }


    @Cacheable("top_games")
    public List<Game> getTopGames() {
        return twitchApiClient.getTopGames().data();
    }


    @Cacheable("games_by_name")
    public List<Game> getGames(String name) {
        return twitchApiClient.getGames(name).data();
    }

    public List<Stream> getStreams(List<String> gameIds, int first) {
        return twitchApiClient.getStreams(gameIds, first).data().stream()
                .filter(stream -> DEFAULT_LANGUAGE.equals(stream.language()))
                .filter(stream -> {
                    String thumbnailUrl = stream.thumbnailUrl();
                    return thumbnailUrl != null
                            && !thumbnailUrl.isEmpty()
                            && !thumbnailUrl.contains("404_processing")  // Filter out processing thumbnails
                            && !thumbnailUrl.contains("404/404");        // Filter out 404 thumbnails
                })
                .collect(Collectors.toList());
    }


    public List<Video> getVideos(String gameId, int first) {
        int multiple = 10;
        return twitchApiClient.getVideos(gameId, multiple*first).data().stream()
                .filter(video -> DEFAULT_LANGUAGE.equals(video.language()))
                .filter(video -> {
                    String thumbnailUrl = video.thumbnailUrl();
                    return thumbnailUrl != null
                            && !thumbnailUrl.isEmpty()
                            && !thumbnailUrl.contains("404_processing")
                            && !thumbnailUrl.contains("404/404");
                })
                .limit(first)
                .collect(Collectors.toList());
    }


    public List<Clip> getClips(String gameId, int first) {
        int multiple = 3;
        return twitchApiClient.getClips(gameId, multiple*first).data().stream()
                .filter(clip -> DEFAULT_LANGUAGE.equals(clip.language()))
                .filter(clip -> {
                    String thumbnailUrl = clip.thumbnailUrl();
                    return thumbnailUrl != null
                            && !thumbnailUrl.isEmpty()
                            && !thumbnailUrl.contains("404_processing")
                            && !thumbnailUrl.contains("404/404");
                })
                .limit(first)
                .collect(Collectors.toList());
    }


    public List<String> getTopGameIds() {
        List<String> topGameIds = new ArrayList<>();
        for (Game game : getTopGames()) {
            topGameIds.add(game.id());
        }
        return topGameIds;
    }
}
