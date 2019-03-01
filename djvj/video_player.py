"""
video_player displays videos that are determined by interpreter.py
"""
import os
import cv2 as visual


class VideoPlayer:
    """
    VideoPlayer is the primary class for playing videos
    It takes a Show
    """

    def __init__(self, show):
        self.curr_video = ""
        self.show = show
        self.window_x = 700
        self.window_y = 900

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
                    # rotate the video
                    frame = visual.warpAffine(
                        frame, rotation_matrix, (width, height))
                #######################################################
                    # resize the frame
                    frame = visual.resize(
                        frame, (self.window_y, self.window_x))
                    visual.namedWindow("window", visual.WND_PROP_FULLSCREEN)
                    visual.setWindowProperty(
                        "window", visual.WND_PROP_FULLSCREEN, visual.WINDOW_FULLSCREEN)

                    # show the frame
                    visual.imshow('window', frame)
                except:
                    cap.release()
                    pass

                if visual.waitKey(1) & 0xFF == ord('q'):
                    break
