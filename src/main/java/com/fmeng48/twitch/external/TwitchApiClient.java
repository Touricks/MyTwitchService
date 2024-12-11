package com.fmeng48.twitch.external;


import com.fmeng48.twitch.external.model.GameResponse;
import com.fmeng48.twitch.external.model.StreamResponse;
import com.fmeng48.twitch.external.model.VideoResponse;
import com.fmeng48.twitch.external.model.ClipResponse;
import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;


import java.util.List;


@FeignClient(name = "twitch-api")
public interface TwitchApiClient {


    @GetMapping("/games")
    GameResponse getGames(@RequestParam("name") String name);


    @GetMapping("/games/top")
    GameResponse getTopGames();


    @GetMapping("/videos")
    VideoResponse getVideos(
            @RequestParam(value = "game_id") String gameId,
            @RequestParam(value = "first") int first);


    @GetMapping("/clips")
    ClipResponse getClips(@RequestParam("game_id") String gameId, @RequestParam("first") int first);


    @GetMapping("/streams")
    StreamResponse getStreams(@RequestParam("game_id") List<String> gameIds, @RequestParam("first") int first);
}
