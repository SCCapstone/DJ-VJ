""" main run file for the project"""
import djvj.djvj_GUI as gui
import djvj.show as show

# initialize GUI
gui.init()

# once a show is loaded, audio_attr/video_attr is initialized
print("This will be passed to the audio listener: %s" % gui.audio_attr)

print("This will be passed to the video instance: %s" % gui.video_attr)

# get show params from gui
show_params = gui.video_attr

# initialize show
show = show.Show(show_params)
