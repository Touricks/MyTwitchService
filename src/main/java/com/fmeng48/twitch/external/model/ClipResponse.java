package com.fmeng48.twitch.external.model;


import java.util.List;


public record ClipResponse(
        List<Clip> data
) {
}
