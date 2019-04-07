"""
video_player displays videos that are determined by interpreter.py

__author__ = "Matthew J. Smith, Lothrop Richards, Timothy Dyar"
__email__ = "mjs10@email.sc.edu, lothropr@email.sc.edu, tdyar@email.sc.edu"
"""
import os
import cv2 as visual
import djvj.show as show
import djvj.audio_listener as audio
import djvj.interpreter as interpreter
import sys

class VideoPlayer:
    """
    VideoPlayer is the primary class for playing videos
    It takes a Show
    """
    def __init__(self, show):
        self.curr_video = None
        self.show = show
        self.window_x = 1920
        self.window_y = 1080
        self.switch = False

    def play_video(self):
        """
        play_video checks if the Show's current video has been updated and plays
        the current video
        """
        def pause():
            # release current video
            cap.release()
            # closes playing window
            visual.destroyAllWindows()
            # gives file paths
            my_path = os.path.abspath(os.path.dirname(__file__))
            # saves path for black image
            black_image = os.path.join(my_path, "../test/test_assets/black.jpg")
            #fullscreen
            # reads image
            image = visual.imread(black_image)
            visual.namedWindow('black_image', visual.WND_PROP_FULLSCREEN)
            visual.setWindowProperty('black_image', visual.WND_PROP_FULLSCREEN, visual.WINDOW_FULLSCREEN)
            # display image
            visual.imshow("black image", image)
            while True:
                #if r key is clicked exit out of black image and display current playing video
                if visual.waitKey(1) & 0xFF == ord('r'):
                    visual.destroyAllWindows()
                    break
            return

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
            visual.namedWindow('video', visual.WND_PROP_FULLSCREEN)
            visual.setWindowProperty('video', visual.WND_PROP_FULLSCREEN, visual.WINDOW_FULLSCREEN)
            # main playback loop - plays the video
            while cap.isOpened():
                # check if current video has been updated
                if self.curr_video != self.show.curr_video:
                    break  # if so, break to update player current video

                # get next frame: returns bool, image
                _, frame = cap.read()

                # Not needed for horizontal videos
                """
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
                    # rotate the video
                    frame = visual.warpAffine(
                        frame, rotation_matrix, (width, height))
                #######################################################
                """
                # resize the frame
                #frame = visual.resize(frame, (self.window_y, self.window_x))
                    # show the frame
                visual.imshow('video', frame)
                """
                except:
                    cap.release()
                    pass
                """
                #pause if condition
                if visual.waitKey(1) & 0xFF == ord('p'):
                    pause()
                    cap = visual.VideoCapture(video)
                #exit program if condition
                if visual.waitKey(1) & 0xFF == ord('k'):
                    #ends audio thread within the audio_listener.py file
                    audio.Off()
                    #ends interpreter thread within the interpreter file
                    interpreter.Off()
                    #closes existing window
                    visual.destroyAllWindows()
                    sys.exit()

                    

