#! /usr/bin/env python3

"""
Iterpreter decides which video should be played based
on the conditions met through the dadaframe
"""
import os
import pandas as pd
#import cv2

class Interpreter:
    """
        Interpreter will find the video file to play based on input
    """
    def __init__(self, show, values, df):
        self.show = show
        self.df = df
        self.curr_pitch = self.show.curr_param_values['pitch']
        # self.curr_tempo = self.show.curr_param_values['tempo']
        # self.curr_time = self.show.curr_param_values['time']
        self.window_x = 700
        self.window_y = 900

    def search_panda_data(self):
        """
		    searchPandaData: Takes in the dataframe called df along with another object
		    Line 37: The for loop will walk through the dataframe row by row
		    Line 39,48,55: The dataframe will first check for only the operator
					       of <,>, or =. if it can not find any of those operators,
					       the dataframe will not pursue any further executions
		    Line (40,43,46),
			     (49,51,53),
			     (56,58,60): The dataframe will use the operator it found from previous
			 			     if statement to comapare the values of Pitch, Tempo, and Time
			 			     that can found within the dataframe
        """
        for index, row in self.df.iterrows():

            if row['Sign'] == '=':
                if self.curr_pitch == int(row['Pitch']) and self.curr_pitch != None:
                    break

                elif self.curr_tempo == int(row['Tempo']) and self.curr_tempo != None:
                    break

                elif self.curr_time == int(row['Time']) and self.curr_time != None:
                    break
            elif row['Sign'] == '>':
                if self.curr_pitch > int(row['Pitch']) and self.curr_pitch != None:
                    break
                elif self.curr_tempo > int(row['Tempo']) and self.curr_tempo != None:
                    break
                elif self.curr_time > int(row['time']) and self.curr_time != None:
                    break
            elif row['Sign'] == '<':
                if self.curr_pitch < int(row['Pitch']) and self.curr_pitch != None:
                    break
                elif self.curr_tempo < int(row['Tempo']) and self.curr_tempo != None:
                    break
                elif self.curr_time < int(row['Time']) and self.curr_time != None:
                    break
