package com.fmeng48.twitch.model;


import com.fmeng48.twitch.db.entity.ItemEntity;


public record FavoriteRequestBody(
        ItemEntity favorite
) {}
