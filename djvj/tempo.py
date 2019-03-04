#! /usr/bin/env python3
"""
Tempo utilizes aubio's tempo analysis function

__author__ = "Matthew J. Smith"
__email__ = "mjs10@email.sc.edu"
"""

from aubio import tempo
import numpy


class Tempo:
    """
    Tempo sets up an instance of aubio's tempo analyzer
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

        # create aubio tempo instance
        self.tempo_analyzer = tempo(
            "specdiff", self.window_size, self.hop_size, self.input.samplerate)

        # slice of beats to keep up with beats over time
        self.beats = []

        # keep up with current tempo
        self.curr_tempo = 0

    def analyze_tempo(self, sample):
        """
        analyze_tempo takes in a sample and analzes the beat of that sample
        """
        # get beat from sample
        is_beat = self.tempo_analyzer(sample)

        # if has a beat
        if is_beat:
            this_beat = self.tempo_analyzer.get_last_s()

            # add beat to list of beats
            self.beats.append(this_beat)

            # if have at least 4 beats, analyze
            if len(self.beats) > 4:
                # analyze tempo
                self.curr_tempo = int(beats_to_bpm(self.beats))

                # remove beats that were analyzed
                del self.beats[0]

                # return bpm
                return self.curr_tempo
        # if not enough beats to analyze, return last known value
        return self.curr_tempo


def beats_to_bpm(beats):
    """
    beats_to_bpm takes in a list of beats and returns the bpm
    """
    # if enough beats are found, convert to periods then to bpm
    bpms = 60. / numpy.diff(beats)
    return numpy.median(bpms)
