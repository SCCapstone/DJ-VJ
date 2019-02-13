#! /usr/bin/env python3
"""
audio_listner is the main driver for analyzing audio
"""

import time
import pyaudio
import numpy
import djvj.pitch as pitch
import djvj.tempo as tempo


class AudioListener:
    """
    sets up instances of audio analyzers
    """

    def __init__(self, audio_params):
        self.audio_input = Microphone()
        self.window_size = 4096
        self.hop_size = 512

        self.listen_params = set(audio_params)  # gets unique values from list

        if 'pitch' in self.listen_params:
            self.pitch = pitch.Pitch(
                self.audio_input, self.window_size, self.hop_size)
        if 'tempo' in self.listen_params:
            self.tempo = tempo.Tempo(
                self.audio_input, self.window_size, self.hop_size)

    def __del__(self):
        self.audio_input.stream.stop_stream()
        self.audio_input.stream.close()
        self.audio_input.pyaudio_instance.terminate()

    def analyze(self, show):
        """
        analyze() is the main loop for analyzing audio
        """
        # get show start time
        start_time = time.time()

        while True:
            try:
                # get next sample
                audiobuffer = self.audio_input.stream.read(
                    self.audio_input.buffer_size, exception_on_overflow=False)
                # convert sample to list
                sample = numpy.frombuffer(audiobuffer, dtype=numpy.float32)

                """
                the following code checks to see if a current feature is being
                listened for, if it is it analyzes and adds to
                show.curr_param_values

                show.curr_param_values = {
                    'pitch': <curr_value>,
                    'tempo': <curr_value>,
                    'volume': <curr_value>.
                    'time:' <curr_value>
                }
                """
                if 'pitch' in self.listen_params:
                    # analyze sample for aubio's pitch (currently in Hz) and update current value
                    show.curr_param_values['pitch'] = self.pitch.analyze_pitch(
                        sample)

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
