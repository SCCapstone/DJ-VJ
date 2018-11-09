#! /usr/bin/env python3
"""This program takes in a .wav file and analyzes and
returns the pitch per sample"""

import sys
from math import log2
import pyaudio
import numpy
from aubio import source, pitch

# Microphone sets up instances of pyaudio required to listen
# to audio via the built in microphone


class Microphone:
    def __init__(self):
        # initialise pyaudio
        self.pyaudio_instance = pyaudio.PyAudio()

        # open stream
        self.buffer_size = 512
        self.pyaudio_format = pyaudio.paFloat32
        self.n_channels = 1
        self.samplerate = 44100
        self.stream = self.pyaudio_instance.open(format=self.pyaudio_format,
                                                 channels=self.n_channels,
                                                 rate=self.samplerate,
                                                 input=True,
                                                 frames_per_buffer=self.buffer_size)
        self.outputsink = None
        self.record_duration = None

# PitchDetection sets up an instances from aubio necessary for aubio analysis
# initalizes aubio source and aubio pitch


class PitchDetection:
    def __init__(self, filename):
        # define each sample size
        # fft size - basically resolution of samples, in multiples of 1024
        # the higher the resolution, the more computation time needed
        self.window_size = 1024

        # hop size - the size of each sample
        # 512 required, otherwise pitch_object returns error
        self.hop_size = 512

        # create aubio source instance
        self.stream = source(filename)
        # get source's sample rate
        self.samplerate = self.stream.samplerate

        # create aubio pitch instance
        # default is yinfft algorithm
        # options = default, schmitt, fcomb, mcomb, yin
        self.pitch_object = pitch(
            "default", self.window_size, self.hop_size, self.samplerate)
        # set to return frequencies, options = Hz, midi
        self.pitch_object.set_unit("Hz")
        # set pitch measurement tolerance
        self.pitch_object.set_tolerance(0.8)

    # analyze_pitch iterates through the audio samples and
    # returns the pitch of each sample

    def analyze_pitch(self):
        # process file
        while True:
            # get next samples, update read marker from source
            samples, read = self.stream()
            # get frequency from sample
            freq = self.pitch_object(samples)[0]
            # if sample has a frequency
            if freq > 0:
                # get and print the pitch
                print(get_pitch(freq))
            # if not enough samples to read, at end of file
            if read < self.hop_size:
                break

# LivePitchDetection takes in an instance of a microphone
# sets up an instances from aubio necessary for aubio analysis
# initalizes aubio source and aubio pitch


class LivePitchDetection:
    def __init__(self, microphone):
        # define input
        self.input = microphone

        # define each sample size
        # fft size - basically resolution of samples, in multiples of 1024
        # the higher the resolution, the more computation time needed
        self.window_size = 4096

        # hop size - the size of each sample
        # 512 required, otherwise pitch_object returns error
        self.hop_size = 512

        # create aubio pitch instance
        # default is yinfft algorithm
        # options = default, schmitt, fcomb, mcomb, yin
        self.pitch_object = pitch(
            "default", self.window_size, self.hop_size, self.input.samplerate)
        # set to return frequencies, options = Hz, midi
        self.pitch_object.set_unit("Hz")
        # set pitch measurement tolerance
        self.pitch_object.set_tolerance(0.8)

    # analyze_pitch listens on an audio stream (microphone) and
    # returns the pitch of each sample

    def analyze_pitch(self):
        print("Listening")
        # process input
        while True:
            try:
                audiobuffer = self.input.stream.read(
                    self.input.buffer_size)
                signal = numpy.frombuffer(audiobuffer, dtype=numpy.float32)

                freq = self.pitch_object(signal)[0]

                # if sample has a frequency
                if freq > 0:
                    # get and print the pitch
                    print(get_pitch(freq))

                if self.input.outputsink:
                    self.input.outputsink(signal, len(signal))

            except KeyboardInterrupt:
                break
        self.input.stream.stop_stream()
        self.input.stream.close()
        self.input.pyaudio_instance.terminate()


def get_attr(attr_name):
    """ called in the GUI, lets audio listener know what attributes to listen for """
    print("These are the audio attributes that are being listened for: ")
    for e in attr_name:
        print(e)  # right now, just prints to console, but can be utilized however

    # after this, would probably be good to start listening for audio


# get_pitch takes an integer representing a frequency (in Hz) and
# returns the musical note representation of that frequency
def get_pitch(freq):
    # equations and formulas based on musical note mathematical theory
    # example is found here:
    # https://www.johndcook.com/blog/2016/02/10/musical-pitch-notation/

    # define tuning, standard is A4 = 440 Hz
    a_4 = 440
    # find C0 based on tuning
    c_0 = a_4 * pow(2, -4.75)
    # define note names
    name = ["C", "C#", "D", "D#", "E", "F",
            "F#", "G", "G#", "A", "A#", "B"]
    # find number of half steps from C0
    half_steps = round(12 * log2(freq / c_0))
    # find the correct octave
    octave = half_steps // 12
    # find the index of the note
    name_index = half_steps % 12
    # return note name with correct octave
    return name[name_index] + str(octave)


if __name__ == '__main__':
    # get .wav file argument
    if len(sys.argv) > 1:
        INPUT = sys.argv[1]
        # create pitch detection instance
        PITCH_DETECTION = PitchDetection(INPUT)
    else:
        # create microphone input instance
        INPUT = Microphone()
        # create pitch detection instance
        PITCH_DETECTION = LivePitchDetection(INPUT)

    # analyze audio
    PITCH_DETECTION.analyze_pitch()
