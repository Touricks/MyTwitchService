package com.fmeng48.twitch.db.entity;


import com.fasterxml.jackson.annotation.JsonProperty;
import com.fmeng48.twitch.external.model.Clip;
import com.fmeng48.twitch.external.model.Stream;
import com.fmeng48.twitch.external.model.Video;
import com.fmeng48.twitch.model.ItemType;
import org.springframework.data.annotation.Id;
import org.springframework.data.relational.core.mapping.Table;

@Table("items")
public record ItemEntity(
        @Id Long id,
        @JsonProperty("twitch_id") String twitchId,
        String title,
        String url,
        @JsonProperty("thumbnail_url") String thumbnailUrl,
        @JsonProperty("broadcaster_name") String broadcasterName,
        @JsonProperty("game_id") String gameId,
        @JsonProperty("item_type") ItemType type
) {


    public ItemEntity(String gameId, Video video) {
        this(null, video.id(), video.title(), video.url(), video.thumbnailUrl(), video.userName(), gameId, ItemType.VIDEO);
    }

    public ItemEntity(Clip clip) {
        this(null, clip.id(), clip.title(), clip.url(), clip.thumbnailUrl(), clip.broadcasterName(), clip.gameId(), ItemType.CLIP);
    }

    public ItemEntity(Stream stream, String url) {
        this(null, stream.id(), stream.title(), url, stream.thumbnailUrl(), stream.userName(), stream.gameId(), ItemType.STREAM);
    }

    public ItemEntity(Stream stream){
        this(null, stream.id(), stream.title(), null, stream.thumbnailUrl(), stream.userName(), stream.gameId(), ItemType.STREAM);
    }
}
