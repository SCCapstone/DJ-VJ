import cv2
import sys
import os
import threading
import djvj.pitch as pitch


class Visual:
    """docstring for ClassName"""

    def __init__(self):
        # initalize current pitch
        self.curr_pitch = 0
        # initialize resource lock
        self.lock = threading.Lock()

    def play_video(self, lock):
        while True:
            lock.acquire()
            if self.curr_pitch < 150:
                lock.release()

                cv2.destroyAllWindows()

                MY_PATH = os.path.abspath(os.path.dirname(__file__))
                PATH = os.path.join(
                    MY_PATH, "../test/video1.mp4")
                CAP = cv2.VideoCapture(PATH)
                CAP.release()

                FRAME, _ = CAP.read()

                cv2.imshow('frame', FRAME)

            elif self.curr_pitch > 150:
                lock.release()
                cv2.destroyAllWindows()

                MY_PATH = os.path.abspath(os.path.dirname(__file__))
                PATH = os.path.join(
                    MY_PATH, "../test/video2.mp4")
                CAP = cv2.VideoCapture(PATH)
                CAP.release()

                FRAME, _ = CAP.read()

                cv2.imshow('frame', FRAME)
