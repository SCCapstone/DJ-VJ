"""

 This program is an example of interacting with images based off a specific condition
 for the DJ-VJ project

 """

import cv2
import sys


while True:

    X = input("Would you like to see a photo ")
    if X == 'yes':
        Y = int(input("which photo would you like to see (ENTER: 0 OR 1): "))
        FILE = repr(Y)+'.jpg'
        IMG = cv2.imread(FILE)
        cv2.imshow('image', IMG)
        cv2.waitKey(3000)
        cv2.destroyAllWindows()
    elif X == 'no':
        sys.exit(0)
