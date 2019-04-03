#! /usr/bin/env python3
"""
show is the primary driver for the program
allows for data to be shared between the different components of the program

__author__ = "Matthew J. Smith"
__email__ = "mjs10@email.sc.edu"
"""

import threading
import os
import time
import audio_listener as audio
import interpreter as interpreter
import video_player as video_player
import sys
import cv2
# import djvj.visual as video
# from djvj.visual import play_video
# from djvj.visual import Visual

class Show:
    """
    Show sets up an instance of a show and initalizes instances of
    needed functions
    """

    def __init__(self, moments):
        """
        moments = list of Moments class
        """
        # list of Moments
        self.moments = moments
        # get listening params
        self.params = []
        for moment in moments:
            self.params += moment.params

        # initialize list of current audio values at a given moment of time
        # populated in audio_listener
        self.curr_param_values = {}

        # initialze audio listener, takes a Show
        self.audio_listener = audio.AudioListener(self)

        # initialize interpreter
        self.interpreter = interpreter.Interpreter(self)

        # initialze video_player, takes a Show
        self.curr_video = ""  # video that should be currently playing
        self.video_player = video_player.VideoPlayer(self)

    def start(self):
        """
        start() starts the show
        """
        global audio_thread
        global interpreter_thread

        try:
            # start audio_listener thread
            # updates show.curr_param_values
            audio_thread = threading.Thread(
                target=self.audio_listener.analyze, args=(self,))
            audio_thread.start()

            # make video decision
            # updates show.curr_video
            interpreter_thread = threading.Thread(
                target=self.interpreter.interpret)
            interpreter_thread.start()

            # start video player
            # compares show.curr_video to video_player.curr_video and
            # updates accordingly
            self.video_player.play_video()

        except KeyboardInterrupt:
            pass



        
