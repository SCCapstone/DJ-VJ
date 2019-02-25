""" main run file for the project"""
import pandas as pd
import djvj.gui as gui
import djvj.show as show

# initialize GUI
gui.init()

# once a show is loaded, audio_attr/video_attr is initialized
# print("This will be passed to the audio listener: %s" % gui.audio_attr)
#
# print("This will be passed to the video instance: %s" % gui.video_attr)

# get show params from gui: [[params], [rules], [values], [videos]]
SHOW_PARAMS = [gui.show[0],
               gui.show[1], gui.show[2], gui.show[3]]
"""
    Line 24: inittialize dataframe 
    Line (26,29,32): stores value of each param into the dataframe.
                     if the value was not specify, the dataframe will
                     set the cell to null
    Line(27,30,33): add values to dataframe
"""

# gui.IntroScreen().quit()

# SHOW_PARAMS = [['pitch', 'tempo', 'volume', 'time'],
#                ['<', '>', '=', '='], [500, 120, 20, 5200], ['']]

# initialize show
SHOW = show.Show(SHOW_PARAMS)

# start show
SHOW.start()
