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


class Moment:

    def __init__(self, name, params, operators, values, video):
        self.name = name
        self.params = params
        self.operators = operators
        self.values = values
        self.video = video


# one param test
# MOMENT_1 = Moment("moment1", ['time'], ['<'], [10],
#                   "/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video1.MOV")
# MOMENT_2 = Moment("moment2", ['time'], ['>'], [10],
#                   "/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video2.mp4")
# SHOW_PARAMS = [MOMENT_1, MOMENT_2]

# two param test, doesnt make sense after 10 seconds
# MOMENT_1 = Moment("moment1", ['time', 'pitch'], ['<', '<'], [10, 500],
#                   "/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video1.MOV")
# MOMENT_2 = Moment("moment2", ['time', 'pitch'], ['<', '>'], [10, 500],
#                   "/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video2.mp4")
# SHOW_PARAMS = [MOMENT_1, MOMENT_2]

# pitch rules reverse after 10 seconds
MOMENT_1 = Moment("moment1", ['time', 'pitch'], ['<', '<'], [15, 500],
                  "/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video1.MOV")
MOMENT_2 = Moment("moment2", ['time', 'pitch'], ['<', '>'], [15, 500],
                  "/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video2.mp4")
MOMENT_3 = Moment("moment3", ['time', 'pitch'], ['>', '<'], [15, 500],
                  "/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video2.mp4")
MOMENT_4 = Moment("moment4", ['time', 'pitch'], ['>', '>'], [15, 500],
                  "/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video1.MOV")
SHOW_PARAMS = [MOMENT_1, MOMENT_2, MOMENT_3, MOMENT_4]

# initialize GUI
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

gui.init()
# print(gui.moments)
MOMENTS = moment.create_moments(gui.moments)

# gui_moments_list = [[['pitch', '<', '500', '/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video1.MOV'], ['time', '<', '10', '/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video1.MOV']], [['pitch', '>', '500', '/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video2.mp4'], ['time', '<', '10', '/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video2.mp4']],
#                     [['pitch', '<', '500', '/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video2.mp4'], ['time', '>', '10', '/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video2.mp4']], [['pitch', '>', '500', '/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video1.MOV'], ['time', '>', '10', '/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video1.MOV']], []]
#
# MOMENTS = moment.create_moments(gui_moments_list)


# SHOW_PARAMS = [['pitch', 'pitch'],
#                ['<', '>'], [500, 500], ["/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video1.MOV", "/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video2.mp4"]]

# SHOW_PARAMS = [['tempo', 'tempo'],
#                ['<', '>'], [120, 120], ["/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video1.MOV", "/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video2.mp4"]]

# SHOW_PARAMS = [['time', 'time'],
#                ['<', '>'], [10, 10], ["/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video1.MOV", "/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video2.mp4"]]

# SHOW_PARAMS = [['pitch', 'time', 'pitch', 'time'],
#
#                ['<', '<', '>', '<'],
#
#                [500, 10, 500, 10],
#
#                ["/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video1.MOV",
#                 "/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video1.MOV",
#                 "/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video2.mp4",
#                 "/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video2.mp4"]]
"""
need instance of videos???? to account for multiple of the same parameter for one video

or make interpreter param based instead of video
"""
"""
During first 30 seconds, pitch < 500 video1, pitch > 500 video2
During second 30 seconds, pitch < 500 video1, pitch > 500 video1

0: if pitch < 500 video1
1: if time < 30 video1
2: if pitch > 500 video2
3: if time < 30 video2

4: if pitch < 500 video2
5: if time > 30 video2
6: if pitch > 500 video1
7: if time > 30 video1
"""

# SHOW_PARAMS = [['pitch', 'time', 'pitch', 'time', 'pitch', 'time', 'pitch', 'time'],
#
#                ['<', '<', '>', '<', '<', '>', '>', '>'],
#
#                [500, 30, 500, 30, 500, 30, 500, 30],
#
#                ["/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video1.MOV",
#                 "/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video1.MOV",
#                 "/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video2.mp4",
#                 "/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video2.mp4",
#                 "/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video2.mp4",
#                 "/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video2.mp4",
#                 "/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video1.MOV",
#                 "/Users/matt/USC/CSCE_490/DJ-VJ/test/test_assets/video1.MOV"]]


# initialize show
#SHOW = show.Show(SHOW_PARAMS)
SHOW = show.Show(MOMENTS)


# start show
# SHOW.start()
