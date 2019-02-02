#! /usr/bin/env python3
import pyaudio
import djvj.pitch as pitch
import numpy


class AudioListener:
    def __init__(self, audio_params):
        self.audio_input = Microphone()
        self.window_size = 4096
        self.hop_size = 512

        self.listen_params = set(audio_params)  # gets unique values from list

        if 'pitch' in self.listen_params:
            self.pitch = pitch.Pitch(
                self.audio_input, self.window_size, self.hop_size)

    def __del__(self):
        self.input.stream.stop_stream()
        self.input.stream.close()
        self.input.pyaudio_instance.terminate()


def analyze(self):
    # list of current aubio values: [frequency, tempo]
    self.curr_audio_values = []

    try:
        # get next sample
        audiobuffer = self.input.stream.read(
            self.input.buffer_size, exception_on_overflow=False)
        # convert sample to list
        sample = numpy.frombuffer(audiobuffer, dtype=numpy.float32)

        if 'pitch' in self.listen_params:
            # analyze sample for aubio's pitch (currently in Hz)
            self.curr_audio_values[0] = self.pitch.analyze_pitch(sample)
    except KeyboardInterrupt:


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
