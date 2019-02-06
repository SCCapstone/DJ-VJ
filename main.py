""" main run file for the project"""
import djvj.djvj_GUI as gui
import djvj.show as show

# initialize GUI
gui.init()

# once a show is loaded, audio_attr/video_attr is initialized
# print("This will be passed to the audio listener: %s" % gui.audio_attr)
#
# print("This will be passed to the video instance: %s" % gui.video_attr)

# get show params from gui: [[params], [rules], [values], [videos]]
print(gui.video_attr)
SHOW_PARAMS = [['pitch', 'tempo', 'volume'],
               [''], [gui.video_attr[0][1]], ['']]

# SHOW_PARAMS = [['pitch', 'tempo', 'volume'],
#                [''], [500], ['']]

# initialize show
SHOW = show.Show(SHOW_PARAMS)

# start show
SHOW.start()
