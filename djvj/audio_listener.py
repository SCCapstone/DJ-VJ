#! /usr/bin/env python3
"""
audio_listner is the main driver for analyzing audio
"""

import time
import pyaudio
import numpy
import djvj.pitch as pitch
import djvj.tempo as tempo
import djvj.chord_detection.chromagram as chromagram
# import djvj.averager as averager


class AudioListener:
    """
    sets up instances of audio analyzers
    """

    def __init__(self, show):
        self.audio_input = Microphone()
        self.window_size = 4096  # needed for pyaudio and aubio
        self.hop_size = 512  # needed for pyaudio and aubio

        self.listen_params = set(show.params)  # gets unique values from list

        # check for listening param and initalize necessary objects
        # also populate show.curr_param_values dictionary
        # if 'chord' in self.listen_params:
        #     self.chromagram = chromagram.PyChromagram(
        #         self.hop_size, self.audio_input.samplerate)

        if 'pitch' in self.listen_params:
            self.pitch = pitch.Pitch(
                self.audio_input, self.window_size, self.hop_size)
            show.curr_param_values['pitch'] = 0

        if 'tempo' in self.listen_params:
            self.tempo = tempo.Tempo(
                self.audio_input, self.window_size, self.hop_size)
            show.curr_param_values['tempo'] = 0

        if 'volume' in self.listen_params:
            show.curr_param_values['volume'] = 0

        if 'time' in self.listen_params:
            show.curr_param_values['time'] = 0

        # initialize averager - used to find average of data
        # self.max_samples = 10 # number of samples collected to find true average
        # self.averager = averager.Averager(self.max_samples)

    def __del__(self):
        self.audio_input.stream.stop_stream()
        self.audio_input.stream.close()
        self.audio_input.pyaudio_instance.terminate()

    def analyze(self, show):
        """
        analyze() is the main loop for analyzing audio
        """
        # get show start time
        if 'time' in self.listen_params:
            start_time = time.time()

        while True:
            try:
                # get next sample
                audiobuffer = self.audio_input.stream.read(
                    self.audio_input.buffer_size, exception_on_overflow=False)
                # convert sample to numpy array
                sample = numpy.frombuffer(audiobuffer, dtype=numpy.float32)

                if 'chord' in self.listen_params:
                    self.chromagram = chromagram.PyChromagram(
                        self.hop_size, self.audio_input.samplerate)
                    self.chromagram.processAudioFrame(sample)
                    if self.chromagram.isReady:
                        print(self.chromagram.getChromagram())

                if 'pitch' in self.listen_params:
                    # analyze sample for aubio's pitch (currently in Hz)
                    curr_pitch = self.pitch.analyze_pitch(sample)
                    # add to average and find current true average
                    # curr_pitch = self.averager.update_average(curr_pitch)
                    # update current value
                    show.curr_param_values['pitch'] = curr_pitch

                if 'tempo' in self.listen_params:
                    # analyze sample for aubio's tempo and update current value
                    show.curr_param_values['tempo'] = self.tempo.analyze_tempo(
                        sample)

                if 'volume' in self.listen_params:
                    # analyze sample for volume and update current value
                    show.curr_param_values['volume'] = int(
                        (numpy.sum(sample**2) / len(sample)) * 60000)

                if 'time' in self.listen_params:
                    # find elapsed timed
                    elapsed_time = time.time() - start_time
                    # update current value
                    show.curr_param_values['time'] = elapsed_time

            except KeyboardInterrupt:
                break


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
