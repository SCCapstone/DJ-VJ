#! /usr/bin/env python3

"""
show is the primary driver for the program
allows for data to be shared between the different components of the program
"""

import threading
import djvj.audio_listener as audio
import djvj.visual as video


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

        # TODO initialize interpreter
        # self.interpreter = interpreter.Interpreter(show_params)

        # initialze audio listener
        self.audio_listener = audio.AudioListener(self.params)

        # TODO Update this with new VideoPlayer class
        # will pass just self.interpreter.curr_video
        self.video_player = video.Visual(self, self.values)

        # initialize list of current audio values at a given moment of time
        # [pitch, tempo, volume, time]
        self.curr_param_values = {
            'pitch': 0,
            'tempo': 0,
            'volume': 0,
            'time': 0
        }

    def start(self):
        """
        start() starts the show
        """
        #  start audio_listener thread
        # updates self.curr_param_values
        try:
            audio_thread = threading.Thread(
                target=self.audio_listener.analyze, args=(self,))
            audio_thread.start()

        except KeyboardInterrupt:
            pass

        # main show loop
        while True:

            if self.curr_param_values['pitch'] != 0:
                print(self.curr_param_values)
            # play video
            self.video_player.play_video()
