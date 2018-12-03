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
        self.pitch_threshold = int(video_attr[0][1])    # placeholder for now, but the value from the param file

    def play_video(self):
        """ plays the video """
        # if the current pitch is > than threshold (from .djvj file)
        if self.curr_pitch > self.pitch_threshold:
            print(self.curr_pitch)
            print("Video 1")
            my_path = os.path.abspath(os.path.dirname(__file__))
            path = os.path.join(my_path, "../test/video1.MOV")
            cap = cv2.VideoCapture(path)    # open first video
            while cap.isOpened():
                if self.curr_pitch < self.pitch_threshold:  # if pitch changes, change video
                    print("break video 1")
                    break
                ret, frame = cap.read()     # play video
                try:
                    cv2.imshow('video', frame)
                except:
                    pass
                    cap.release()
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    print("BREAK")
                    break

        # if the current pitch is < than threshold (from .djvj file)
        if self.curr_pitch < self.pitch_threshold:
            print("Video 2")
            my_path = os.path.abspath(os.path.dirname(__file__))
            path = os.path.join(my_path, "../test/video2.mp4")
            cap = cv2.VideoCapture(path)    # open second video
            while cap.isOpened():
                if self.curr_pitch > self.pitch_threshold:  # if pitch changes, change video
                    print("break video 2")
                    break
                ret, frame = cap.read()
                try:
                    cv2.imshow('video', frame)      # play video
                except:
                    pass
                    cap.release()
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    print("BREAK")
                    break
