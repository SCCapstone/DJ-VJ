import unittest
from Visual import Visual
import os
import cv2
import time

class TestParameters(unittest.TestCase):

	def setUp(self):
        self.visual_object = Visual(20, 1920, 1080)

	   ## self.curr_pitch = 20
	   ## self.window_x = 1920
	   ## self.window_y = 1080

	    self.visual_object.pitch_threshold = int(video_attr[0][1])
    
    def tearDown(self):
    	pass

    def testparam(self):
        self.assertEqual(self.curr_pitch)
        self.assertEqual(self.window_x)
        self.assertEqual(self.window_y)

        self.visual_object.curr_pitch = 10000
        self.visual_object.window_x = 2560
        self.visual_object.window_y = 1440

        self.assertEqual(self.curr_pitch)
        self.assertEqual(self.window_x)
        self.assertEqual(self.window_y)

        self.visual_object.curr_pitch = 20000
        self.visual_object.window_x = 3840
        self.visual_object.window_y = 2160

        self.assertEqual(self.curr_pitch)
        self.assertEqual(self.window_x)
        self.assertEqual(self.window_y)


if __name__ == '__main__':
	unittest.main()