""" main run file for the project"""
import djvj.djvj_GUI as gui
import djvj.pitch as audio_listener
import sys

# initialize GUI
gui.init()

# once a show is loaded, audio_attr/video_attr is initialized
print("This will be passed to the audio listener: %s" % gui.audio_attr)

print("This will be passed to the video instance: %s" % gui.video_attr)

# initialize audio listener
# check if have .wav file argument
if len(sys.argv) > 1:
    # create .wav file audio listener
    INPUT = sys.argv[1]
    audio_listener = audio_listener.Audio_Listener(
        gui.audio_attr, "wav", INPUT)
else:
    # create live audio listener
    audio_listener = audio_listener.Audio_Listener(gui.audio_attr, "live")
