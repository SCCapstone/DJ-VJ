"""
This program displays videos based on the audio input passed
from the audio listener.
"""
import os
import time
import cv2


class Visual:
    """Main class in the file, creates the video"""

    def __init__(self, video_attr):
        """ initialize the class """
        self.curr_pitch = 0
        self.window_x = 700
        self.window_y = 900
        # placeholder for now, but the value from the param file
        self.pitch_threshold = int(video_attr[0][1])

    def play_video(self):
        """ plays the video """
        # if the current pitch is > than threshold (from .djvj file)
        if self.curr_pitch > self.pitch_threshold:
            my_path = os.path.abspath(os.path.dirname(__file__))
            path = os.path.join(my_path, "../test/video1.MOV")
            cap = cv2.VideoCapture(path)    # open first video
            print("now here")
            while cap.isOpened():
                if self.curr_pitch < self.pitch_threshold:  # if pitch changes, change video
                    break
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
                    pass
                    cap.release()
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        # if the current pitch is < than threshold (from .djvj file)
        if self.curr_pitch < self.pitch_threshold:
            my_path = os.path.abspath(os.path.dirname(__file__))
            path = os.path.join(my_path, "../test/video2.mp4")
            cap = cv2.VideoCapture(path)    # open second video
            print("i'm here")
            while cap.isOpened():
                if self.curr_pitch > self.pitch_threshold:  # if pitch changes, change video
                    break
                ret, frame = cap.read()
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
                    pass
                    cap.release()
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
