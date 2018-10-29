"""
changes images for application .
user can change images bases on the number they input

"""
import cv2

for x in xrange(0, 3):
    file = repr(x)+'.jpg'
    img = cv2.imread(file)
    cv2.imshow('image', img)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()
