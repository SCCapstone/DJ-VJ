#! /usr/bin/env python3

"""
show is the primary driver for the program
allows for data to be shared between the different components of the program
"""

import threading
import djvj.audio_listener as audio
import djvj.Visual as video


class Show:
    """
    Show sets up an instance of a show and initalizes instances of
    needed functions
    """

    def __init__(self, show_params):
        self.params = show_params[0]
        self.rules = show_params[1]
        self.values = show_params[2]
        self.videos = show_params[3]

        # self.interpreter = interpreter.Interpreter(show_params)
        self.audio_listener = audio.AudioListener(self.params)
        self.video_player = video.Visual(self, self.values)

        # initialize list of current audio values at a given moment of time
        # [pitch, tempo, volume]
        self.curr_audio_values = [0, 0, 0]

    def start(self):
        """
        start() starts the show
        """
        #  start audio_listener thread
        # updates self.curr_audio_values
        try:
            audio_thread = threading.Thread(
                target=self.audio_listener.analyze, args=(self,))
            audio_thread.start()

        except KeyboardInterrupt:
            pass

        # main show loop
        while True:
            if self.curr_audio_values[0] != 0:
                print(self.curr_audio_values)

            # play video
            self.video_player.play_video()
