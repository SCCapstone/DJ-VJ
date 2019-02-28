"""
This program displays videos based on the audio input passed
from the audio listener.
"""
import cv2
import threading


class Visual:
    """Main class in the file, creates the video"""

    def __init__(self):
        """ initialize the class """
        self.currShow = None
        self.window_x = 700
        self.window_y = 900
        # placeholder for now, but the value from the param file
        #threshold = values[0]
        #self.pitch_threshold = int(threshold)
        #current show playing and the new show that we want to play
        #self.newShow = None

def play_video(self, video):
    """ plays the video """
    #my_path = os.path.abspath(os.path.dirname(__file__))
    #self.newShow = video
    if self.currShow == None:
        self.currShow = video
    elif self.currShow == video:
        pass
    else:
        self.currShow = video
    #path = os.path.join(my_path, "../test/test_assets/video1.MOV")
    cap = cv2.VideoCapture(self.currShow)    # open first video
    # print("now here")
    while cap.isOpened():
        #if self.currShow != video:
             #self.currShow = video
             #cap.cv2.VideoCapture(self.currShow)
        ret, frame = cap.read()     # play video
        try:
            (h, w) = frame.shape[:2]
            center = (w / 2, h / 2)
        except:
            break
        try:
            M = cv2.getRotationMatrix2D(center, -90, 1.0)
            frame = cv2.warpAffine(frame, M, (w, h))  # rotate video
            frame = cv2.resize(frame, (self.window_y, self.window_x))
            cv2.imshow('video', frame)  # play video
        except:
            cap.release()
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
