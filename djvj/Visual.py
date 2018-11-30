import cv2
import sys
import os
import djvj.pitch as pitch


class Visual:
    """docstring for ClassName"""

    def __init__(self):
        self.curr_pitch = 0

    def play_video(self):
        while True:
            if self.curr_pitch < 150:

                cv2.destroyAllWindows()

                MY_PATH = os.path.abspath(os.path.dirname(__file__))
                PATH = os.path.join(
                    MY_PATH, "/Users/matt/USC/CSCE_490/DJ-VJ/test/video1.mp4")
                CAP = cv2.VideoCapture(PATH)
                CAP.release()

                FRAME, _ = CAP.read()

                cv2.imshow('frame', FRAME)

            elif self.curr_pitch > 150:
                cv2.destroyAllWindows()

                MY_PATH = os.path.abspath(os.path.dirname(__file__))
                PATH = os.path.join(
                    MY_PATH, "/Users/matt/USC/CSCE_490/DJ-VJ/test/video2.mp4")
                CAP = cv2.VideoCapture(PATH)
                CAP.release()

                FRAME, _ = CAP.read()

                cv2.imshow('frame', FRAME)
