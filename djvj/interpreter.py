#! /usr/bin/env python3

"""
Iterpreter decides which video should be played based
on the conditions met through the dataframe
"""
import os
import pandas as pd
#import cv2

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
        self.flag_time = 0
        self.flag_tempo = 0
        self.flag_pitch = 0
    
    def creating_master_frame(self):
        self.mf = iterate_master_frame(self.df, self.mf)
        return self.mf

    def search_panda_data(self):

        if 'pitch' in self.show.curr_param_values:
            self.curr_pitch = self.show.curr_param_values['pitch']
        if 'tempo' in self.show.curr_param_values:
            self.curr_tempo = self.show.curr_param_values['tempo']
        if 'time' in self.show.curr_param_values:
            self.curr_time = self.show.curr_param_values['time']

        print(self.curr_tempo)

        for index, row in self.mf.iterrows():

            if self.curr_pitch != None:
                if row['Pitch'] != None:
                    self.bool_pitch = comapare(row, self.curr_pitch, row['Pitch_Com'], int(row['Pitch']))

                    if self.curr_tempo != None:
                        if row['Tempo'] != None:
                            self.bool_tempo = comapare(row, self.curr_tempo, row['Tempo_Com'], int(row['Tempo']))
                            if self.bool_tempo == self.bool_pitch:
                                continue
                            else:
                                flag_tempo = 1

                    if self.curr_time != None:
                        if row['Time'] != None:
                            self.bool_time = comapare(row, self.curr_time, row['Time_Com'], int(row['Time']))
                            if self.bool_time == self.bool_pitch:
                                continue
                            else:
                                self.flag_time = 1

                    if self.flag_tempo == 1 or self.flag_time == 1 or self.bool_pitch == 1:
                        self.flag_tempo = 0
                        self.flag_time = 0
                        self.bool_pitch = None
                    else:
                        self.flag_tempo = 0
                        self.flag_time = 0
                        return row['File_Path']

            if self.curr_tempo != None:
                if row['Tempo'] != None:
                    self.bool_tempo = comapare(row, self.curr_tempo, row['Tempo_Com'], int(row['Tempo']))

                    if self.curr_pitch != None:
                        if row['Pitch'] != None:
                            self.bool_pitch = comapare(row, self.curr_pitch, row['Tempo_Pitch'], int(row['Pitch']))
                            if self.bool_tempo == self.bool_pitch:
                                continue
                            else:
                                flag_pitch = 1

                    if self.curr_time != None:
                        if row['Time'] != None:
                            self.bool_time = comapare(row, self.curr_time, row['Time_Com'], int(row['Time']))
                            if self.bool_time == self.bool_tempo:
                                continue
                            else:
                                self.flag_time = 1

                    if self.flag_tempo == 1 or self.flag_time == 1 or self.bool_tempo == 1:
                        self.flag_tempo = 0
                        self.flag_time = 0
                        self.bool_pitch = None
                    else:
                        self.flag_tempo = 0
                        self.flag_time = 0
                        return row['File_Path']


            if self.curr_time != None:
                if row['Time'] != None:
                    self.bool_time = comapare(row, self.curr_time, row['Time_Com'], int(row['Time']))

                    if self.curr_pitch != None:
                        if row['Pitch'] != None:
                            self.bool_pitch = comapare(row, self.curr_pitch, row['Pitch_Com'], int(row['Pitch']))
                            if self.bool_pitch == bool_time:
                                continue
                            else:
                                flag_pitch = 1
                    if self.curr_tempo != None:
                        if row['Tempo'] != None:
                            self.bool_tempo = comapare(row, self.curr_tempo, row['Tempo_Com'], int(row['Tempo']))
                            if self.bool_tempo == bool_time:
                                continue
                            else:
                                flag_tempo = 1
                if self.flag_pitch == 1 or self.flag_tempo == 1 or self.curr_time == 1:
                    self.flag_pitch = 0
                    self.flag_tempo = 0
                    self.curr_time = None
                else:
                    self.flag_pitch = 0
                    self.flag_tempo = 0
                    return row['File_Path']


def iterate_master_frame(df, master_df):
    df.to_csv("df.csv")
    for index, row in df.iterrows():
        flag = 0 
        flag = nested_iteration(row, master_df)

        if flag == 0:
            master_df = create_master_frame(df, row['File_Name'], master_df)
            master_df.to_csv("master.csv")

    return master_df

def nested_iteration(cell, master_df):

    for index, row in master_df.iterrows():
        if cell['File_Name'] == row['File_Path']:
            return 1
    return 0

def create_master_frame(df, file, master_df):
    pitch_s = None 
    pitch_v = None
    tempo_s = None 
    tempo_v = None
    time_s = None 
    time_v = None
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

    return master_df.append({'File_Path': file, 'Pitch_Com': pitch_s, 'Pitch': pitch_v,'Tempo_Com': tempo_s, 'Tempo': tempo_v,
                                  'Time_Com': time_s, 'Time':time_v}, ignore_index=True)

def comapare(row, measure, sign, value):

    measure = int(measure)
    value = int(value)
    print(measure, sign, value)

    if sign == '=' and value != None:
        if measure == value:
            return row['File_Path']
    if sign == '>' and value != None:
        if measure > value:
            return row['File_Path']
    if sign == '<' and value != None:
        if measure < value:
            return row['File_Path']
    return 1      









            

