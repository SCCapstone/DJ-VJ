#! /usr/bin/env python3

"""
show is the primary driver for the program
allows for data to be shared between the different components of the program
"""
import threading
import pandas as pd
import djvj.audio_listener as audio
import djvj.visual as video
import djvj.interpreter as interpreter
# import djvj.video_player as video


class Show:
    """
    Show sets up an instance of a show and initalizes instances of
    needed functions
    """

    def __init__(self, show_params, df, master_df):
        self.params = show_params[0]
        self.rules = show_params[1]
        self.values = show_params[2]
        self.videos = show_params[3]
        self.df = df
        self.master_df = master_df
        
        # initialize list of current audio values at a given moment of time
        # populated in audio_listener
        self.curr_param_values = {}

        # initialze audio listener
        self.audio_listener = audio.AudioListener(self)

        # initialize interpreter
        self.data_interperter = interpreter.Interpreter(self, self.values, self.df, self.master_df)
        # initialize master frame
        self.master_df = self.data_interperter.creating_master_frame()
        #reinitialize interpreter with new table
        self.data_interperter = interpreter.Interpreter(self, self.values, self.df, self.master_df)


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
            #returns file name that needs to play
            #video = self.data_interperter.search_panda_data()

            # play video
            self.video_player.play_video()  # remove or update to next comment
            # TODO
            # self.video_player.play_video(video)

def add_panda_data(videos, rules, pitch, tempo, time, df):
    """
        addPandaData ( takes in video file name, comparative operator,
                        pitch value, temp value, time value)
        Line 79: appends data that is givin into dataFrame
    """

    df = df.append({'File_Name' : videos,
                  'Sign' : rules,
                  'Pitch' : pitch,
                  'Tempo' : tempo,
                  'Time' : time}, ignore_index=True)

    return df
