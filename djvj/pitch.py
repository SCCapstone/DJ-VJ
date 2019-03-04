#! /usr/bin/env python3
"""
Pitch utilizes aubio's' pitch analysis function
"""

from math import log2
import numpy
from aubio import pitch


class Pitch:  # pylint: disable=too-few-public-methods
    """
    Pitch sets up an instance of aubio's pitch analyzer
    """

    def __init__(self, audio_input, window_size, hop_size):
        # define input
        self.input = audio_input

        # define each sample size
        # fft size - basically resolution of samples, in multiples of 1024
        # the higher the resolution, the more computation time needed
        self.window_size = window_size

        # hop size - the size of each sample
        # 512 required, otherwise pitch_analyzer returns error
        self.hop_size = hop_size

        # create aubio pitch instance
        # default is yinfft algorithm
        # options = default, schmitt, fcomb, mcomb, yin
        self.pitch_analyzer = pitch(
            "default", self.window_size, self.hop_size, self.input.samplerate)
        
        #saves the average pitch for better accuracy
        self.average = 0

    def analyze_pitch(self, sample):
        """
        analyze_pitch analyzes the pitch of a given audio sample
        """
        freq = self.pitch_analyzer(sample)[0]
        volume = int((numpy.sum(sample**2) / len(sample)) * 60000)
        # confidence = self.pitch_analyzer.get_confidence()

        # if sample has a frequency
        if freq > 0 and volume > 20:
            # get and print the pitch
            return freq

        return 0


def get_pitch(freq):
    """
    get_pitch takes an integer representing a frequency (in Hz) and
    returns the musical note representation of that frequency
    """
    # equations and formulas based on musical note mathematical theory
    # example is found here:
    # https://www.johndcook.com/blog/2016/02/10/musical-pitch-notation/

    # edge cases
    # lowest musical notation or highest humans can hear
    if freq < 16.35 or freq > 20000:
        return ""

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
