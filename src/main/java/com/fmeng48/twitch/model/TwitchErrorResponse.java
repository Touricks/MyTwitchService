package com.fmeng48.twitch.model;


public record TwitchErrorResponse(
        String message,
        String error,
        String details
) {
}
