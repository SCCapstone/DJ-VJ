import numpy 
import cv2
import sys

for x in xrange(0,3):
	file = repr(x)+'.jpg'
	img = cv2.imread(file)
	cv2.imshow('image', img)
	cv2.waitKey(3000)
	cv2.destroyAllWindows();
