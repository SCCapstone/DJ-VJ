'''
Version 3 of app, takes in audio and saves it as a WAV file

in later versions:
	#Allow user to dictate where the recording is saved as well as its name
	#Add a visual effect(soundwave) that depicts the sound being recorded
	#improve GUI/Style
'''

#import tkinter
import subprocess
import tkinter as tk
import tkinter.messagebox
import pyaudio
import wave
import os

# Variables
FILE_LOCATION = 'TODO'
F_NAME = 'temp.wav'

class Recorder:
    def __init__(self, chunk=3024, frmat=pyaudio.paInt16, channels=2, rate=44100,
                 py=pyaudio.PyAudio()):

        # Start Tkinter and set Title
        self.root = tkinter.Tk()
        self.collections = []
        self.root.geometry('600x100')
        self.root.title('SoundSaver')
        self.chunk = chunk
        self.format = frmat
        self.channels = channels
        self.rate = rate
        self.p_var = py
        self.frames = []
        self.st_var = 1
        self.stream = self.p_var.open(format=self.format, channels=self.channels,
                                      rate=self.rate, input=True, frames_per_buffer=self.chunk)

        # Set Frames
        self.buttons = tkinter.Frame(self.root, padx=120, pady=20)

        # Pack Frame
        self.buttons.pack(fill=tk.BOTH)

        # Start and Stop buttons
        self.strt_rec = tkinter.Button(self.buttons, width=10, padx=10, pady=5, text='Record',
                                       command=lambda: self.start_record(), bg="lightblue")
        self.strt_rec.grid(row=0, column=0, padx=5, pady=5)
        self.stop_rec = tkinter.Button(self.buttons, width=10, padx=10, pady=5,
                                       text='Stop', command=lambda: self.stop(), bg="lightblue")
        self.stop_rec.grid(row=0, column=1, columnspan=1, padx=5, pady=5)

        self.root.mainloop()

    def start_record(self):
        self.st_var = 1
        self.frames = []
        stream = self.p_var.open(format=self.format, channels=self.channels, rate=self.rate,
                                 input=True, frames_per_buffer=self.chunk)
        while self.st_var == 1:
            data = stream.read(self.chunk)
            self.frames.append(data)
            print("* recording")
            self.root.update()

        stream.close()
        wf = wave.open(F_NAME, 'wb')
        wf.setnchannels(self.channels)
        wf.setsampwidth(self.p_var.get_sample_size(self.format))
        wf.setframerate(self.rate)
        wf.writeframes(b''.join(self.frames))
        wf.close()

    def stop(self):
        self.st_var = 0
        print("~ finished recording ~")

RecorderGUI = Recorder()
