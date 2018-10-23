#! /usr/bin/env python3
"""
This program takes in a .wav file and analyzes and returns the pitch per sample
"""
import sys
from math import log2, pow
from aubio import source, pitch

"""
get_pitch takes in a frequency and returns the musical note representation of
that frequency
"""


def get_pitch(freq):
    # equations and formulas based on musical note mathematical theory
    # example is found here:
    # https://www.johndcook.com/blog/2016/02/10/musical-pitch-notation/

    # define tuning, standard is A4 = 440 Hz
    A4 = 440
    # find C0 based on tuning
    C0 = A4 * pow(2, -4.75)
    # define note names
    name = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    # find number of half steps from C0
    half_steps = round(12 * log2(freq / C0))
    # find the correct octave
    octave = half_steps // 12
    # find the index of the note
    n = half_steps % 12
    # return note name with correct octave
    return name[n] + str(octave)


if __name__ == '__main__':
    # get .wav file argument
    filename = sys.argv[1]

    # define each sample size
    # fft size - basically resolution of samples, in multiples of 1024
    # the higher the resolution, the more computation time needed
    window_size = 1024

    # hop size - the size of each sample
    # 512 required, otherwise pitch_object returns error
    hop_size = 512

    # create aubio source instance
    source = source(filename)
    # get source's sample rate
    samplerate = source.samplerate

    # create aubio pitch instance
    # default is yinfft algorithm
    # options = default, schmitt, fcomb, mcomb, yin
    pitch_object = pitch("default", window_size, hop_size, samplerate)
    # set to return frequencies, options = Hz, midi
    pitch_object.set_unit("Hz")
    # set pitch measurement tolerance
    pitch_object.set_tolerance(0.8)

    # process file
    while True:
        # get next samples, update read marker from source
        samples, read = source()
        # get frequency from sample
        freq = pitch_object(samples)[0]
        # if sample has a frequency
        if freq > 0:
            # get and print the pitch
            print(get_pitch(freq))
        # if not enough samples to read, at end of file
        if read < hop_size:
            break
