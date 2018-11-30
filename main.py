""" main run file for the project"""
import sys
import djvj.djvj_GUI as gui
import djvj.pitch as audio_listener
import djvj.Visual as video

# initialize GUI
gui.init()

# once a show is loaded, audio_attr/video_attr is initialized
print("This will be passed to the audio listener: %s" % gui.audio_attr)

print("This will be passed to the video instance: %s" % gui.video_attr)

# initialize Visual
VISUAL = video.Visual()

# initialize audio listener
# check if have .wav file argument
if len(sys.argv) > 1:
    # create .wav file audio listener
    AUDIO_INPUT = sys.argv[1]
    AUDIO_LISTENER = audio_listener.AudioListener(
        gui.audio_attr, "wav", AUDIO_INPUT)
else:
    # create live audio listener
    AUDIO_LISTENER = audio_listener.AudioListener(
        gui.audio_attr, "live", VISUAL)


AUDIO_LISTENER.pitch_detection.analyze_pitch(AUDIO_LISTENER.VISUAL)
VISUAL.play_video()
