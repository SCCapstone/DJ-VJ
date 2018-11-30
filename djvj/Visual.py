import cv2
import sys
import os


class Visual:
    """docstring for ClassName"""
    def __init__(self, Pitch):
        
        self.input = Pitch

        while True:
            if self.input < 150 :

                cv2.destroyAllWindows()

                MY_PATH = os.path.abspath(os.path.dirname(__file__))
                PATH = os.path.join(MY_PATH, "../test/video1.mp4")
                CAP = cv2.VideoCapture(PATH)
                CAP.release()

                FRAME = CAP.read()

                cv2.imshow('frame', FRAME)

            elif self.input > 150 :
                cv2.destroyAllWindows()

                MY_PATH = os.path.abspath(os.path.dirname(__file__))
                PATH = os.path.join(MY_PATH, "../test/video2.mp4")
                CAP = cv2.VideoCapture(PATH)
                CAP.release()
                
                FRAME = CAP.read()

                cv2.imshow('frame', FRAME)

        
