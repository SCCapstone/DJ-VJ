"""
video_player displays videos that are determined by interpreter.py

__author__ = "Matthew J. Smith, Lothrop Richards, Timothy Dyar"
__email__ = "mjs10@email.sc.edu, lothropr@email.sc.edu, tdyar@email.sc.edu"
"""
import os
import numpy as np
import tkinter
import cv2 as visual


class VideoPlayer:
    """
    VideoPlayer is the primary class for playing videos
    It takes a Show
    """

    def __init__(self, show):
        self.curr_video = ""  # keeps track of the current video to be played
        self.show = show  # show instance that is using this video_player

        # get screen dimensions
        root = tkinter.Tk()
        self.window_x = root.winfo_screenheight()
        self.window_y = root.winfo_screenwidth()

        # signals
        self.pause = False  # keeps track if video is paused
        self.kill = False  # keeps track if video_player is killed

    def play_video(self):
        """
        play_video checks if the Show's current video has been updated and plays
        the current video
        """

        # update video loop
        while True:
            # initialze current video
            self.curr_video = self.show.curr_video
            # get current path
            my_path = os.path.abspath(os.path.dirname(__file__))
            # add video path to current path
            video = os.path.join(my_path, self.curr_video)
            # open video
            cap = visual.VideoCapture(video)

            # main playback loop - plays the video
            while cap.isOpened():
                # check signals
                # if pause
                if self.pause:
                    # release current video
                    cap.release()
                    # closes playing window
                    visual.destroyAllWindows()
                    # pause the video
                    self.pause_video()
                    # after unpausing, open video
                    cap = visual.VideoCapture(video)

                # if kill
                if self.kill:
                    # closes existing window
                    visual.destroyAllWindows()
                    # exit video_player
                    return

                # check if current video has been updated
                if self.curr_video != self.show.curr_video:
                    break  # if so, break to update player current video

                # get next frame: returns bool, image
                _, frame = cap.read()

                # resize the frame
                frame = visual.resize(
                    frame, (self.window_y, self.window_x))
                # create window
                visual.namedWindow("window", visual.WND_PROP_FULLSCREEN)
                # make window full screen
                visual.setWindowProperty(
                    "window", visual.WND_PROP_FULLSCREEN, visual.WINDOW_FULLSCREEN)
                # show the frame
                visual.imshow('window', frame)

                # get waitKey value
                key = visual.waitKey(1)

                # if have waitKey, check what key was pressed
                if key & 0xFF == ord('p'):
                    # set pause video bool
                    self.pause = True
                elif key & 0xFF == ord('k'):
                    # set kill video_player bool
                    self.kill = True
                    return

    def pause_video(self):
        """
        pause_video displays a black image when the user pauses the show
        by pressing 'p'
        """

      # saves path for black image
      black_image = np.zeros(
            [self.window_x, self.window_y, 3], dtype=np.uint8)
       black_image.fill(0)

        # create window
        visual.namedWindow("window", visual.WND_PROP_FULLSCREEN)
        # make window full screen
        visual.setWindowProperty(
            "window", visual.WND_PROP_FULLSCREEN, visual.WINDOW_FULLSCREEN)
            # get waitKey value
            key = visual.waitKey(1)
            # if r key is clicked exit out of black image and display current playing video
            if key & 0xFF == ord('r'):
                self.pause = False
                visual.destroyAllWindows()
                break
            # if k is pressed, kill program
            elif key & 0xFF == ord('k'):
                self.kill = True
                return
        return


def resource_path(relative_path):
    """
    Get absolute path to resource, works for dev and for PyInstaller

    src: https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file
    """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
