#! /usr/bin/env python3

"""
Iterpreter decides which video should be played based
on the conditions met through the dadaframe
"""
import os
import pandas as pd
#import cv2

global pitch_s
global pitch_v
global tempo_s
global tempo_v
global time_s
global time_v

class Interpreter:
    """
        Interpreter will find the video file to play based on input
    """
    def __init__(self, show, values, df, master_df):
        self.show = show
        self.df = df
        self.mf = master_df
        self.window_x = 700
        self.window_y = 900
        if 'pitch' in self.show.curr_param_values:
            self.curr_pitch = self.show.curr_param_values['pitch']
            self.curr_tempo = None
            self.curr_time = None
        if 'tempo' in self.show.curr_param_values:
            self.curr = self.show.curr_param_values['tempo']
            self.curr_pitch = None
            self.curr_time = None
        if 'time' in self.show.curr_param_values:
            self.curr_time = self.show.curr_param_values['time']
            self.curr_pitch = None
            self.curr_tempo = None

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

        master_frame(self.df, self.mf)

        print(master_df)


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
                elif self.curr_time > int(row['Time']) and self.curr_time != None:
                    
                    break
            elif row['Sign'] == '<':
                if self.curr_pitch < int(row['Pitch']) and self.curr_pitch != None:
                    
                    break
                elif self.curr_tempo < int(row['Tempo']) and self.curr_tempo != None:
                    
                    break
                elif self.curr_time < int(row['Time']) and self.curr_time != None:
                    
                    break
    
    def iterate_master_frame(df, master_df):
        for index, row in df.iterrows():
            pitch_s, pitch_v,
            temp_s, tempo_v,
            time_s, time_v = None

            flag = 0

            df_file = row['File_Name'] 

            for index, row in master_df.iterrows():
                if df_file == row['File_Path']:
                    flag = 1

            if flag == 0:
                create_master_frame(df, row['File_Name'])

                master_df = master_df.append('File_Path': row['File_Name'] 
                                            'Pitch_Com': pitch_s, 'Pitch': pitch_v,
                                            'Tempo_Com': tempo_s, 'Tempo': tempo_v, 
                                            'Time_Com': time_s, 'Time': time_v, ignore_index=True)

    def create_master_frame(df, file):
        for index, row in df.iterrows():
            if row['File_Name'] == file:
                if row['Pitch'] != None:
                    pitch_s = row['Sign']
                    pitch_v = row['Pitch']

                elif row['Tempo'] != None:
                    tempo_s = row['Sign']
                    tempo_v = row['Tempo']

                elif row['Time'] != None:
                    time_s = row['Sign']
                    time_v = row['Time']





            

