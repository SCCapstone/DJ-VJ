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
        self.pitch_s = None
        self.pitch_v = None
        self.tempo_s = None
        self.tempo_v = None
        self.time_s = None
        self.time_v = None
        self.flag_time = 0
        self.flag_tempo = 0
        self.flag_pitch = 0
        if 'pitch' in self.show.curr_param_values:
            self.curr_pitch = self.show.curr_param_values['pitch']
        if 'tempo' in self.show.curr_param_values:
            self.curr = self.show.curr_param_values['tempo']
        if 'time' in self.show.curr_param_values:
            self.curr_time = self.show.curr_param_values['time']
    
    def creating_master_frame(self):
        self.mf = iterate_master_frame(self, self.mf,)
        return mf

    def search_panda_data(self):

        for index, row in self.mf.iterrows():

            if self.curr_pitch != None:  
                self.bool_pitch = comapare(row, self.curr_pitch, row['Pitch_Com'], int(row['Pitch']))

                if self.curr_tempo != None:
                    self.bool_tempo = comapare(row, self.curr_pitch, row['Pitch_Com'], int(row['Pitch']))
                    if self.bool_tempo == self.bool_pitch:
                        continue
                    else:
                        flag_tempo = 1
                if self.curr_time != None:
                    self.bool_time = comapare(row, self.curr_pitch, row['Pitch_Com'], int(row['Pitch']))
                    if self.bool_time == self.bool_pitch:
                        continue
                    else:
                        self.flag_time = 1

                if self.flag_tempo == 1 or self.flag_time == 1 or self.curr_pitch == 1:
                    self.flag_tempo = 0
                    self.flag_time = 0
                    break
                else:
                    self.flag_tempo = 0
                    self.flag_time = 0
                    return self.bool_pitch

            if self.curr_tempo != None:
                self.bool_tempo = comapare(row, self.curr_tempo, row['Tempo_Com'], int(row['Tempo']))

                if self.curr_pitch != None:
                    self.bool_pitch = comapare(row, self.curr_pitch, row['Pitch_Com'], int(row['Pitch']))
                    if self.bool_pitch == self.bool_tempo:
                        continue
                    else:
                        flag_pitch = 1
                if self.curr_time != None:
                    self.bool_time = comapare(row, self.curr_pitch, row['Pitch_Com'], int(row['Pitch']))
                    if self.bool_time == self.bool_tempo:
                        continue
                    else:
                        flag_time = 1
                if self.flag_pitch == 1 or self.flag_time == 1 or self.curr_tempo == 1:
                    self.flag_pitch = 0
                    self.flag_time = 0
                    break
                else:
                    self.flag_pitch = 0
                    self.flag_time = 0
                    return self.bool_tempo

            if self.curr_time != None:
                self.bool_time = comapare(row, self.curr_tempo, row['Tempo_Com'], int(row['Tempo']))

                if self.curr_pitch != None:
                    self.bool_pitch = comapare(row, self.curr_pitch, row['Pitch_Com'], int(row['Pitch']))
                    if self.bool_pitch == bool_time:
                        continue
                    else:
                        self.bool_pitch = 1
                if self.curr_time != None:
                    self.bool_time = comapare(row, self.curr_pitch, row['Pitch_Com'], int(row['Pitch']))
                    if self.bool_tempo == bool_time:
                        continue
                    else:
                        self.bool_tempo = 1
                if self.flag_pitch == 1 or self.flag_tempo == 1 or self.curr_time == 1:
                    self.flag_pitch = 0
                    self.flag_tempo = 0
                else:
                    self.flag_pitch = 0
                    self.flag_tempo = 0
                    return bool_time

def iterate_master_frame(df, master_df):
    pitch_s = None 
    pitch_v = None 
    tempo_s = None
    tempo_v = None
    time_s = None
    time_v = None

    for index, rowA in df.iterrows():
        pitch_s = None 
        pitch_v = None
        tempo_s = None 
        tempo_v = None
        time_s = None 
        time_v = None
        flag = 0
        df_file = rowA['File_Name']

        for index, rowB in master_df.iterrows():
            master_df = create_master_frame(df, rowA['File_Name'], master_df)
            print('HOLLA')
            if df_file == rowB['File_Path']:
                flag = 1
            else:
                print(master_df)
                master_df = create_master_frame(df, row['File_Name'], master_df)
                print(master_df)
    return master_df

def create_master_frame(df, file, master_df):
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

    master_df = master_df.append({'File_Path': file, 'Pitch_Com': self.pitch_s, 'Pitch': self.pitch_v,'Tempo_Com': self.tempo_s, 'Tempo': self.tempo_v,
                                  'Time_Com': self.time_s, 'Time': self.time_v}, ignore_index=True)
    print(master_df)

    # return master_df.append({'File_Path': file, 'Pitch_Com': self.pitch_s, 'Pitch': self.pitch_v,
    #                          'Tempo_Com': self.tempo_s, 'Tempo': self.tempo_v, 
    #                          'Time_Com': self.time_s, 'Time': self.time_v}, ignore_index=True)

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









            

