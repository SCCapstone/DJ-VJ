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
        self.curr_tempo = None
        self.curr_time = None
        self.curr_pitch = None
        self.bool_pitch = None
        self.bool_tempo = None
        self.bool_tempo = None
        if 'pitch' in self.show.curr_param_values:
            self.curr_pitch = self.show.curr_param_values['pitch']
        if 'tempo' in self.show.curr_param_values:
            self.curr = self.show.curr_param_values['tempo']
        if 'time' in self.show.curr_param_values:
            self.curr_time = self.show.curr_param_values['time']

    def search_panda_data(self):

        iterate_master_frame(self.df, self.mf)

        print(self.mf)

        for index, row in self.mf.iterrows():

            if self.curr_pitch != None:  
                bool_pitch = comapare(row, self.curr_pitch, row['Pitch_Com'], int(row['Pitch']))

                if self.curr_tempo != None:
                    bool_tempo = comapare(row, self.curr_pitch, row['Pitch_Com'], int(row['Pitch']))
                    if bool_tempo == bool_pitch:
                        continue
                    else:
                        flag_tempo = 1

                if self.curr_time != None:
                    bool_time = comapare(row, self.curr_pitch, row['Pitch_Com'], int(row['Pitch']))
                    if bool_time == bool_pitch:
                        continue
                    else:
                        flag_time = 1

                if flag_tempo == 1 or flag_time == 1 or curr_pitch:
                    flag_tempo = 0
                    flag_time = 0
                    break
                else:
                    flag_tempo = 0
                    flag_time = 0
                    return bool_pitch

            if self.curr_tempo != None:
                bool_tempo = comapare(row, self.curr_tempo, row['Tempo_Com'], int(row['Tempo']))

                if self.curr_pitch != None:
                    bool_pitch = comapare(row, self.curr_pitch, row['Pitch_Com'], int(row['Pitch']))
                    if bool_pitch == bool_tempo:
                        continue
                    else:
                        flag_pitch = 1

                if self.curr_time != None:
                    bool_time = comapare(row, self.curr_pitch, row['Pitch_Com'], int(row['Pitch']))
                    if bool_time == bool_tempo:
                        continue
                    else:
                        flag_time = 1

                if flag_pitch == 1 or flag_time == 1 or self.curr_tempo:
                    flag_pitch = 0
                    flag_time = 0
                    break
                else:
                    flag_pitch = 0
                    flag_time = 0
                    return bool_tempo

            if self.curr_time != None:
                bool_time = comapare(row, self.curr_tempo, row['Tempo_Com'], int(row['Tempo']))

                if self.curr_pitch != None:
                    bool_pitch = comapare(row, self.curr_pitch, row['Pitch_Com'], int(row['Pitch']))
                    if bool_pitch == bool_time:
                        continue
                    else:
                        bool_pitch = 1

                if self.curr_time != None:
                    bool_time = comapare(row, self.curr_pitch, row['Pitch_Com'], int(row['Pitch']))
                    if bool_tempo == bool_time:
                        continue
                    else:
                        bool_tempo = 1

                if flag_pitch == 1 or flag_tempo == 1 or self.curr_time == 1:
                    flag_pitch = 0
                    flag_tempo = 0
                else:
                    flag_pitch = 0
                    flag_tempo = 0
                    return bool_time

def comapare(row, measure, sign, value):
    if sign == '=':
        if measure == value:
            return row['File_Name']
    elif sign == '>':
        if measure > value:
            return row['File_Name']
    elif sign == '<':
        if measure < value:
            return row['File_Name']
    else:
        return 1

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
           elif flag == 0:
               create_master_frame(df, row['File_Name'])
               master_df = master_df.append({'File_Path': row['File_Name'], 
                                             'Pitch_Com': pitch_s, 'Pitch': pitch_v,
                                             'Tempo_Com': tempo_s, 'Tempo': tempo_v, 
                                             'Time_Com': time_s, 'Time': time_v}, ignore_index=True)

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





            

