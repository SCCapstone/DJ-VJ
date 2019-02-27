"""
This program displays videos based on the audio input passed
from the audio listener.
"""
import os
#import cv2
import time
from visual import Visual
from visual import play_video

show = Visual()
#Play the first video
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../test/test_assets/video1.MOV")
play_video(show, path)
time.sleep(5) #5 second delay
#Send the same video again to see if original video keeps playing
play_video(show, path)
time.sleep(3)
#Send new video to see if it changes
path = os.path.join(my_path, "../test/test_assets/video2.mp4")
play_video(show, path)
