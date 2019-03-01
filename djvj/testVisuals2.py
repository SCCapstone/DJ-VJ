import os
import threading
import cv2
import time
from visual import Visual
from visual import play_video


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
show.newShow = path1
n = 0

print("Try first video")
first = threading.Thread(target=play_video, args=(show,))
first.start()
#daShow = play_video(show)
time.sleep(3)
print("Try the second show")
show.newShow = path2
#daShow = play_video(show)
first = threading.Thread(target=play_video, args=(show))
print("We did it!")
#playVideo = threading.Thread(target=play_video, args=(show, videoList[0]))
"""
while n != 2:
	print("Whats up")
	newPath = videoList[n]
	play_video(show, newPath)
	print("FUCKING STAB ME")
	n = n + 1
	print("WHY AM I STILL BREATHING")
print("Done")
"""