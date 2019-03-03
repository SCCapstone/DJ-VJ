#! /usr/bin/env python3

"""
show is the primary driver for the program
allows for data to be shared between the different components of the program
"""

import threading
import time
import djvj.audio_listener as audio
import djvj.interpreter as interpreter
import djvj.video_player as video_player
# import djvj.interpreter as interpreter
# import djvj.video_player as video


class Show:
    """
    Show sets up an instance of a show and initalizes instances of
    needed functions
    """

    def __init__(self, moments):
        self.moments = moments
        # get listening params
        self.params = []
        for moment in moments:
            self.params = self.params + moment.params

        # initialize list of current audio values at a given moment of time
        # populated in audio_listener
        self.curr_param_values = {}

        # initialze audio listener, takes a Show
        self.audio_listener = audio.AudioListener(self)

        # TODO initialize interpreter
        self.interpreter = interpreter.Interpreter(self)

        # initialze video_player, takes a Show
        self.curr_video = ""  # video that should be currently playing
        self.video_player = video_player.VideoPlayer(self)

    def start(self):
        """
        start() starts the show
        """
        threads = []

        try:
            # start audio_listener thread
            # updates show.curr_param_values
            print("Listening")
            audio_thread = threading.Thread(
                target=self.audio_listener.analyze, args=(self,))
            audio_thread.start()
            threads.append(audio_thread)

            # make video decision
            # updates show.curr_video
            print("Interpreting")
            interpreter_thread = threading.Thread(
                target=self.interpreter.interpret)
            interpreter_thread.start()
            threads.append(interpreter_thread)

            # temporary interpreter for testing video player
            # interpreter_thread = threading.Thread(
            #     target=tmp_interpreter, args=(self,))
            # interpreter_thread.start()
            # threads.append(interpreter_thread)

            # start video player
            # compares show.curr_video to video_player.curr_video and
            # updates accordingly
            print("Playing video")
            self.video_player.play_video()

        except KeyboardInterrupt:
            # for thread in threads:
            #     thread.event.set()
            # audio_thread.join(timeout=None)
            # interpreter_thread.join(timeout=None)
            pass


def tmp_interpreter(show):
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
        time.sleep(4)
