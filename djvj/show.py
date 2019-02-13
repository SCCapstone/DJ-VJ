#! /usr/bin/env python3

"""
show is the primary driver for the program
allows for data to be shared between the different components of the program
"""

import threading
import djvj.audio_listener as audio
import djvj.visual as video
# import djvj.interpreter as interpreter
# import djvj.video_player as video


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

        # initialize list of current audio values at a given moment of time
        # populated in audio_listener
        self.curr_param_values = {}

        # initialze audio listener
        self.audio_listener = audio.AudioListener(self)

        # TODO initialize interpreter
        # self.interpreter = interpreter.Interpreter(show_params)

        # TODO initialze video_player
        # Update this with new VideoPlayer class
        # self.video_player = video.VideoPlayer()

        # only used for current visual.py
        self.video_player = video.Visual(self, self.values)

    def start(self):
        """
        start() starts the show
        """
        # start audio_listener thread
        # updates self.curr_param_values
        try:
            audio_thread = threading.Thread(
                target=self.audio_listener.analyze, args=(self,))
            audio_thread.start()

        except KeyboardInterrupt:
            pass

        # main show loop
        while True:

            # TODO
            # make video decision
            # video = self.interpreter.make_decision(self.curr_param_values)

            # play video
            self.video_player.play_video()  # remove or update to next comment
            # TODO
            # self.video_player.play_video(video)
