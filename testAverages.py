from math import log2
from pitchAverager import pitchAverager

"""
Testing the pitchAverager function
"""
print ("test 1")
testValues = [1, 2, 3, 4, 5, 6, 7 , 8 , 9 , 10]
for x in range (0, 10):
    currAvg = pitchAverager(testValues[x])
    print (currAvg)
print (currAvg)
"""
Try again for a new average
"""
print ("test two")
testValues = [11, 12, 13, 14, 15, 16, 17 , 18 , 19 , 20]
for x in range (0, 10):
    currAvg = pitchAverager(testValues[x])
    print (currAvg)
print (currAvg)


