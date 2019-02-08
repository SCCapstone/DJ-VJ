"""
Runs a simple behavioral test.
As the user, I wish to be able to load the program,
view the splash screen and then have the main screen
with the options to Create or Load Show available to select.
"""

import time
import djvj.gui as gui

if __name__ == '__main__':
    print("Start Test")
    gui.IntroScreen()
    time.sleep(5)
    exit(0)
