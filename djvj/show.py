#! /usr/bin/env python3
"""
show is the primary driver for the program
allows for data to be shared between the different components of the program
"""

import threading
import os
import time
import djvj.audio_listener as audio
import djvj.visual as video
from djvj.visual import play_video
from djvj.visual import Visual


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

        # new visual.py
        # MY INITIALIZING THE VISUALS CLASS TO KEEP TRACK OF THE CURRENT SHOW
        self.play_video = video.Visual()

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

        # testing loop for updating video
        interpreter_thread = threading.Thread(
            target=tmp_interpreter, args=(self,))
        interpreter_thread.start()

        # main show loop
        while True:
            play_video(self.play_video)


def tmp_interpreter(show):
    # temp videos
    my_path = os.path.abspath(os.path.dirname(__file__))
    # Set the video paths for the video
    path1 = os.path.join(my_path, "../test/test_assets/video1.MOV")
    path2 = os.path.join(my_path, "../test/test_assets/video2.mp4")
    num = "1"
    while True:
        if num == "1":
            show.curr_video = path1
            show.play_video.newShow = path1
            num = "2"
        else:
            show.curr_video = path2
            show.play_video.newShow = path2
            num = "1"
        print(show.curr_video)
        time.sleep(3)
