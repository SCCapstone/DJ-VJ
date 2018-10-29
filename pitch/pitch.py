#! /usr/bin/env python3
"""This program takes in a .wav file and analyzes and
returns the pitch per sample"""

import sys
from math import log2
from aubio import source, pitch

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
    FILENAME = sys.argv[1]

    # create pitch detection instance
    PITCH_DETECTION = PitchDetection(FILENAME)

    # analyze audio
    PITCH_DETECTION.analyze_pitch()
