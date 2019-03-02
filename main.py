#! /usr/bin/env python3
"""
main run file for the project

sets up necessary instances and passing data between GUI and backend

__author__ = "Matthew J. Smith, Abby Holdeman"
__email__ = "mjs10@email.sc.edu, holdeman@email.sc.edu"
"""


# import djvj.gui as gui
import djvj.gui_moments as gui
import djvj.moment as moment
import djvj.show as show

# initialize GUI
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> interpreter working with small shows. not fast enough for larger ones. main is bypassing GUI for testing
# gui.init()

# once a show is loaded, audio_attr/video_attr is initialized
# print("This will be passed to the audio listener: %s" % gui.audio_attr)
#
# print("This will be passed to the video instance: %s" % gui.video_attr)

# get show params from gui: [[params], [rules], [values], [videos]]
# SHOW_PARAMS = [gui.show[0],
#                gui.show[1], gui.show[2], gui.show[3]]

print(gui.moments)
# this is only for testing purposes, show that the file path stays the same

# SHOW_PARAMS = [['pitch', 'pitch'],
#                ['<', '>'], [500, 500], ["/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video1.MOV", "/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video2.mp4"]]
=======
gui.init()
# print(gui.moments)
MOMENTS = moment.create_moments(gui.moments)
>>>>>>> create moment class to handle GUI moments, updated main to reflect moments

# gui_moments_list = [[['pitch', '<', '500', '/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video1.MOV'], ['time', '<', '10', '/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video1.MOV']], [['pitch', '>', '500', '/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video2.mp4'], ['time', '<', '10', '/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video2.mp4']],
#                     [['pitch', '<', '500', '/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video2.mp4'], ['time', '>', '10', '/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video2.mp4']], [['pitch', '>', '500', '/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video1.MOV'], ['time', '>', '10', '/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video1.MOV']], []]
#
# MOMENTS = moment.create_moments(gui_moments_list)


# SHOW_PARAMS = [['pitch', 'pitch'],
#                ['<', '>'], [500, 500], ["/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video1.MOV", "/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video2.mp4"]]

# SHOW_PARAMS = [['tempo', 'tempo'],
#                ['<', '>'], [120, 120], ["/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video1.MOV", "/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video2.mp4"]]

SHOW_PARAMS = [['time', 'time'],
               ['<', '>'], [10, 10], ["/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video1.MOV", "/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video2.mp4"]]

# SHOW_PARAMS = [['pitch', 'time', 'pitch', 'time', 'pitch', 'time', 'pitch', 'time'],
#                ['<', '<', '>', '<', '<', '>', '>', '>'], [500, 30, 500, 30, 500, 30, 500, 30], ["/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video1.MOV", "/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video1.MOV", "/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video2.mp4", "/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video2.mp4", "/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video2.mp4", "/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video2.mp4", "/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video1.MOV", "/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video1.MOV"]]

# initialize show
<<<<<<< HEAD
#SHOW = show.Show(SHOW_PARAMS)
=======
SHOW = show.Show(MOMENTS)
>>>>>>> create moment class to handle GUI moments, updated main to reflect moments

# start show
#SHOW.start()
