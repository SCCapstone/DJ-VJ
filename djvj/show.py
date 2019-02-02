#! /usr/bin/env python3
import djvj.audio_listener as audio


class Show:
    def __init__(self, show_params):
        self.audio_params = show_params[0]
        self.rules = show_params[1]
        self.values = show_params[2]
        self.videos = show_params[3]

        # self.interpreter = interpreter.Interpreter(show_params)
        self.audio_listener = audio.AudioListener(self.audio_params)
