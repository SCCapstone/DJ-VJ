#! /usr/bin/env python3
"""
main run file for the project

sets up necessary instances and passing data between GUI and backend

__author__ = "Matthew J. Smith, Abby Holdeman"
__email__ = "mjs10@email.sc.edu, holdeman@email.sc.edu"
"""


import djvj.gui as gui
import djvj.moment as moment
import djvj.show as show

# # initialize GUI
gui.init()

# print(gui.moments)
MOMENTS = moment.create_moments(gui.moments)

# initialize show
SHOW = show.Show(MOMENTS)
#print(MOMENTS[0].video)
# start show
SHOW.start()
