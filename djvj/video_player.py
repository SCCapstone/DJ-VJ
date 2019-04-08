"""
video_player displays videos that are determined by interpreter.py

__author__ = "Matthew J. Smith, Lothrop Richards, Timothy Dyar"
__email__ = "mjs10@email.sc.edu, lothropr@email.sc.edu, tdyar@email.sc.edu"
"""
import os
import tkinter
import threading
import queue
import numpy as np
import cv2 as visual


class VideoPlayer:
    """
    VideoPlayer is the primary class for playing videos
    It takes a Show
    """

    def __init__(self, show):
        self.curr_video = ""  # keeps track of the current video to be played
        self.switched = False  # keeps up with if video was switched
        self.show = show  # show instance that is using this video_player
        self.queue = queue.Queue(maxsize=100)  # queue to hold loaded frames
        self.cap = visual.VideoCapture()  # video capture object

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

        # create main window for video playback
        visual.namedWindow("window", visual.WND_PROP_FULLSCREEN)
        # make window full screen
        visual.setWindowProperty(
            "window", visual.WND_PROP_FULLSCREEN, visual.WINDOW_FULLSCREEN)

        # update video loop
        while True:
            # initialze current video
            self.curr_video = self.show.curr_video
            # get current path
            my_path = os.path.abspath(os.path.dirname(__file__))
            # add video path to current path
            video = os.path.join(my_path, self.curr_video)
            # open video
            self.cap = visual.VideoCapture(video)
            # update switched
            self.switched = False

            # start queue thread
            queue_thread = threading.Thread(target=queue_frames, args=(self,))
            queue_thread.start()

            # main playback loop - plays the video
            while self.cap.isOpened():
                # check signals
                # if pause
                if self.pause:
                    # release current video
                    self.cap.release()
                    # closes playing window
                    # pause the video
                    self.pause_video()
                    # after unpausing, open video
                    self.cap = visual.VideoCapture(video)

                # if kill
                if self.kill:
                    # closes existing window
                    visual.destroyAllWindows()
                    # exit video_player
                    return

                # check if current video has been updated
                if self.curr_video != self.show.curr_video:
                    # update switched
                    self.switched = True
                    # break to update player current video
                    break

                # check of queue is empty
                if self.queue.qsize() == 0:
                    continue

                # get next frame from queue
                frame = self.queue.get()

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

        # create numpy array of the size of the screen
        black_image = np.zeros(
            [self.window_x, self.window_y, 3], dtype=np.uint8)
        # fill with zeros for black pixels
        black_image.fill(0)

        # display image
        visual.imshow("window", black_image)
        # while showing black
        while True:
            # get waitKey value
            key = visual.waitKey(1)
            # if r key is clicked exit out of black image and display current playing video
            if key & 0xFF == ord('r'):
                self.pause = False
                break
            # if k is pressed, kill program
            elif key & 0xFF == ord('k'):
                self.kill = True
                return
        return


def queue_frames(video_player):
    while not video_player.kill:
        # check if video has been switched
        if video_player.switched is True:
            video_player.queue.empty()
            return
        # check if queue is full
        if video_player.queue.full():
            continue
        # get frame
        _, frame = video_player.cap.read()
        # resize the frame
        frame = visual.resize(
            frame, (video_player.window_y, video_player.window_x))
        # add to queue
        video_player.queue.put(frame)
