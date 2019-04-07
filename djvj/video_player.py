"""
video_player displays videos that are determined by interpreter.py

__author__ = "Matthew J. Smith, Lothrop Richards, Timothy Dyar"
__email__ = "mjs10@email.sc.edu, lothropr@email.sc.edu, tdyar@email.sc.edu"
"""
import os
import sys
import cv2 as visual


class VideoPlayer:
    """
    VideoPlayer is the primary class for playing videos
    It takes a Show
    """

    def __init__(self, show):
        self.curr_video = ""  # keeps track of the current video to be played
        self.show = show  # show instance that is using this video_player
        self.window_x = 700
        self.window_y = 900

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

                #######################################################
                # may not need this code if using horizontal videos
                try:
                    # get height and width
                    (height, width) = frame.shape[:2]
                    # find center
                    center = (width / 2, height / 2)
                except:
                    break

                # our videos default to different orientation
                # need to test other videos
                try:
                    # get rotation matrix
                    rotation_matrix = visual.getRotationMatrix2D(
                        center, -90, 1.0)
                    # # rotate the video
                    frame = visual.warpAffine(
                        frame, rotation_matrix, (width, height))
                    #######################################################
                    # resize the frame
                    frame = visual.resize(
                        frame, (self.window_y, self.window_x))
                #######################################################
                    # possible fullscreen playback code
                    # visual.namedWindow("window", visual.WND_PROP_FULLSCREEN)
                    # visual.setWindowProperty(
                    #     "window", visual.WND_PROP_FULLSCREEN, visual.WINDOW_FULLSCREEN)
                #######################################################
                    # show the frame
                    visual.imshow('window', frame)
                except:
                    cap.release()
                    pass
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

        # get relative path for black.jpg
        black_image = resource_path("black.jpg")
        # reads image
        image = visual.imread(black_image)
        # display image
        visual.imshow("black image", image)
        while True:
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
