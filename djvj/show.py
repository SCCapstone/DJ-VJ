#! /usr/bin/env python3

"""
show is the primary driver for the program
allows for data to be shared between the different components of the program
"""

import threading
import time
import djvj.audio_listener as audio
import djvj.video_player as video_player
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
        self.curr_video = ""  # keep track of which video should be playing
        # self.video_player = video.VideoPlayer()

        # only used for current visual.py
        self.video_player = video_player.VideoPlayer(self)

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

        # TODO
        # make video decision
        # probably spin off on our thread
        # video = self.interpreter.make_decision(self.curr_param_values)

        # play video

        # testing loop for updating video
        interpreter_thread = threading.Thread(target=test, args=(self,))
        interpreter_thread.start()

        # start video player
        self.video_player.play_video()


def test(show):
    # temp videos
    path1 = "../test/test_assets/video1.MOV"
    path2 = "../test/test_assets/video2.mp4"

    num = "1"
    while True:
        if num == "1":
            show.curr_video = path1
            num = "2"
        else:
            show.curr_video = path2
            num = "1"
        # print(show.curr_video)
        time.sleep(2)
