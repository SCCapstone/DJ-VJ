#! /usr/bin/env python3
"""
This program identifies pitches based on an audio input
Currently can support .wav file analysis and real time analysis from a
built in microphone
"""

from math import log2
import pyaudio
import numpy
from aubio import source, pitch


class Microphone:  # pylint: disable=too-few-public-methods

    """
    Microphone sets up instances of pyaudio required to listen
    to audio via the built in microphone
    """

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


class PitchDetection:  # pylint: disable=too-few-public-methods

    """
    PitchDetection sets up an instances from aubio necessary for aubio analysis
    initalizes aubio source and aubio pitch
    """

    def __init__(self, filename):
        # create aubio source instance
        self.input = source(filename)
        # get source's sample rate
        self.samplerate = self.input.samplerate

        # define each sample size
        # fft size - basically resolution of samples, in multiples of 1024
        # the higher the resolution, the more computation time needed
        self.window_size = 1024

        # hop size - the size of each sample
        # 512 required, otherwise pitch_object returns error
        self.hop_size = 512

        # create aubio pitch instance
        # default is yinfft algorithm
        # options = default, schmitt, fcomb, mcomb, yin
        self.pitch_object = pitch(
            "default", self.window_size, self.hop_size, self.samplerate)
        # set to return frequencies, options = Hz, midi
        self.pitch_object.set_unit("Hz")
        # set pitch measurement tolerance
        self.pitch_object.set_tolerance(0.8)

    def analyze_pitch(self):
        """
        analyze_pitch iterates through the audio samples and
        returns the pitch of each sample
        """
        # process file
        while True:
            # get next samples, update read marker from source
            samples, read = self.input()
            # get frequency from sample
            freq = self.pitch_object(samples)[0]
            # if sample has a frequency
            if freq > 0:
                # get and print the pitch
                print(get_pitch(freq))
            # if not enough samples to read, at end of file
            if read < self.hop_size:
                break


class LivePitchDetection:  # pylint: disable=too-few-public-methods
    """
    LivePitchDetection takes in an instance of a microphone
    sets up an instances from aubio necessary for aubio analysis
    initalizes aubio source and aubio pitch
    """

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

    def analyze_pitch(self, visual, lock):
        """
        analyze_pitch listens on an audio stream (microphone) and
        returns the pitch of each sample
        """
        print("NOW LISTENING")
        # process input
        while True:
            try:
                audiobuffer = self.input.stream.read(
                    self.input.buffer_size)
                signal = numpy.frombuffer(audiobuffer, dtype=numpy.float32)

                freq = self.pitch_object(signal)[0]
                # confidence = self.pitch_object.get_confidence()

                # if sample has a frequency
                if freq > 0:
                    # get and print the pitch
                    print(int(freq))
                    # lock resources
                    lock.acquire()
                    visual.curr_pitch = int(freq)
                    # release resources
                    lock.release()
                    # print(confidence)

                if self.input.outputsink:
                    self.input.outputsink(signal, len(signal))

            except KeyboardInterrupt:
                break
        self.input.stream.stop_stream()
        self.input.stream.close()
        self.input.pyaudio_instance.terminate()


def get_pitch(freq):
    """
    get_pitch takes an integer representing a frequency (in Hz) and
    returns the musical note representation of that frequency
    """
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


class AudioListener:  # pylint: disable=too-few-public-methods
    """
    AudioListener is the handler for audio listening request
    Currently only starts listening for pitch
    Future plan is to use is to use to turn on requested listening parameters
    """

    def __init__(self, listening_params, mode, visual, filename=""):
        self.VISUAL = visual
        print("Listening for: ", listening_params)
        if mode == "wav":
            audio_input = filename
            # create pitch detection instance
            self.pitch_detection = PitchDetection(audio_input)
        else:
            # create microphone input instance
            audio_input = Microphone()
            # create pitch detection instance
            self.pitch_detection = LivePitchDetection(audio_input)

        # analyze audio
        # self.pitch_detection.analyze_pitch(self.VISUAL)
