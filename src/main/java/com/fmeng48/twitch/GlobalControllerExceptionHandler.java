package com.fmeng48.twitch;


import com.fmeng48.twitch.favorite.DuplicateFavoriteException;
import com.fmeng48.twitch.model.TwitchErrorResponse;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;

@ControllerAdvice
public class GlobalControllerExceptionHandler {

    @ExceptionHandler(DuplicateFavoriteException.class)
    public final ResponseEntity<TwitchErrorResponse> handleDefaultException(Exception e) {
        return new ResponseEntity<>(
                new TwitchErrorResponse("Duplicate entry error.",
                        e.getClass().getName(),
                        e.getMessage()
                ),
                HttpStatus.BAD_REQUEST
        );
    }
}
