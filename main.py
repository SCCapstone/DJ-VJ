""" main run file for the project"""
import pandas as pd
import djvj.gui as gui
import djvj.show as show

# initialize GUI
gui.init()

print(gui.DF)

# once a show is loaded, audio_attr/video_attr is initialized
# print("This will be passed to the audio listener: %s" % gui.audio_attr)
#
# print("This will be passed to the video instance: %s" % gui.video_attr)

# get show params from gui: [[params], [rules], [values], [videos]]
SHOW_PARAMS = [gui.show[0],
               gui.show[1], gui.show[2], gui.show[3]]

# gui.IntroScreen().quit()

# SHOW_PARAMS = [['pitch', 'tempo', 'volume', 'time'],
#                ['<', '>', '=', '='], [500, 120, 20, 5200], ['']]

# initialize show
SHOW = show.Show(SHOW_PARAMS, gui.DF, gui.master_dF)

# start show
SHOW.start()
