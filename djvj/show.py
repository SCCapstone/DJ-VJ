#! /usr/bin/env python3

from djvj.visual import play_video
from djvj.visual import Visual
import djvj.visual as video
import threading
import os
import time
"""
show is the primary driver for the program
allows for data to be shared between the different components of the program
"""

"""
NOTE:
I COMMENTED OUT ALL THE AUDIO STUFF BECAUSE I HAVEN'T BEEN ABLE TO GET
AUBIO TO INSTALL AND THAT WAS KEEPING ME FROM TESTING.
THAT BEING SAID, IT MAY HAVE BEEN WHAT WAS CAUSE THE GUI TO CRASH FOR ME.
IF YOU HAVE IT INSTALLED, PUT IT BACK IN
"""
#import djvj.audio_listener as audio
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
        # I COMMENTED OUT FOR TESTING
        #self.audio_listener = audio.AudioListener(self)

        # TODO initialize interpreter
        # self.interpreter = interpreter.Interpreter(show_params)

        # TODO initialze video_player
        # Update this with new VideoPlayer class
        # self.video_player = video.VideoPlayer()

        # only used for current visual.py
        #self.video_player = video.Visual(self, self.values)
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
            # I COMMENTED OUT FOR TESTING
            # audio_thread = threading.Thread(
             #   target=self.audio_listener.analyze, args=(self,))
            # audio_thread.start()
            pass

        except KeyboardInterrupt:
            pass
        # testing loop for updating video
        interpreter_thread = threading.Thread(
            target=tmp_interpreter, args=(self,))
        interpreter_thread.start()

        # main show loop
        while True:

            # TODO
            # make video decision (Omaris function)
            # video = self.interpreter.make_decision(self.curr_param_values)

            # Take Omari's video and plays it
            # WHAT I WOULD PUT IN TO RUN WITH OMARI'S FUNCTION TO PLAY THE VIDEO
            # print(self.curr_video)
            play_video(self.play_video)
            # showPlaying = threading.Thread(
            #     target=play_video, args=(self.play_video,))
            # showPlaying.start()

# TEMPORARY FUNCTIONS I MADE TO TEST VIDEO PLAYBACK
# Return functions that should return what video to play like Omari's code


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
        time.sleep(5)


def videoReturns1():
    """
    Returns videos like Omaris function should just for test sake
    """
    my_path = os.path.abspath(os.path.dirname(__file__))
    # Set the video paths for the video
    path1 = os.path.join(my_path, "../test/test_assets/video1.MOV")
    return path1


def videoReturns2():
    """
    Returns videos like Omaris function should just for test sake
    """
    my_path = os.path.abspath(os.path.dirname(__file__))
    # Set the video paths for the video
    path2 = os.path.join(my_path, "../test/test_assets/video2.mp4")
    return path2
