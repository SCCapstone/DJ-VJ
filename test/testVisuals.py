"""
This program displays videos based on the audio input passed
from the audio listener.
"""
import os
import threading
import cv2
import time
from visual import Visual
from visual import play_video

class Test:

	def __init__(self):
		pass
def do_test():
    
    show = Visual()
    #Play the first video
    print("We here")
    videoList = []
    my_path = os.path.abspath(os.path.dirname(__file__))
    path1 = os.path.join(my_path, "../test/test_assets/video1.MOV")
    path2 = os.path.join(my_path, "../test/test_assets/video2.mp4")
    videoList.append(path1)
    videoList.append(path2)
    show.currShow = path1
    n = 0
    playVideo = threading.Thread(target=play_video, args=(show, videoList[0]))
    while n != 2:
    	print("Whats up")
    	newPath = videoList[n]
    	play_video(show, newPath)
    	#playVideo.start()
    	print("Hello")
    	
    	print("Hello Again")
    	n = n + 1
    	#playVideo.args(show, videoList[n])
    	print("hello 1 more time")
    print("Done")
    """
    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path, "../test/test_assets/video2.mp4")
    show.currShow = path
    #playVideo = threading.Thread(target=play_video, args=(show, path))
    #playVideo.start()
    play_video(show, path)
    time.sleep(2) #5 second delay
    print("we back")
    #Send the same video again to see if original video keeps playing
    #play_video(show, path)
    time.sleep(3)
    print("back again")
    #Send new video to see if it changes
    path = os.path.join(my_path, "../test/test_assets/video1.MOV")
    play_video(show, path)
    """

