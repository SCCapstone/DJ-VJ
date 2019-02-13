#! /usr/bin/env python3

"""
video_player is used to play videos

NOTE:
this file will replace the visual.py file or visual.py needs to be updated
"""


class VideoPlayer:

    def __init__(self):
        """
        not sure if we need a whole class for this or if we need to keep up
        with the values below, but we can if necessary
        """
        self.curr_video = ""
        # self.curr_frame = ""

    def play_video(self, video):
        """
        play_video
        - takes in a path to a video
        - determines if continues to play the current video or start playing
        the newly passed video
        - continues playing / plays new video
        """
