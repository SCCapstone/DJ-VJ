from math import log2
from pitchAverager import pitchAverager
from pitchAverager import PitchAvgs
import unittest


"""
Testing the pitchAverager function
"""
class TestPitchAvgs(unittest.TestCase):
    
    def test_avgsmethod(self):
        self = PitchAvgs(1)
        self.pitchArr.append(self.pitch)
        for x in range (1, 10):
            self.pitchArr.append(x)	
        self.lastAvg = pitchAverager(self)
        print(self.lastAvg)

if __name__ == '__main__':
    unittest.main()
"""
print ("test 1")
testValues = [1, 2, 3, 4, 5, 6, 7 , 8 , 9 , 10]
pitch1 = pitchAvgs(0)
for x in range (0, 10):
    currAvg = pitchAverager(testValues[x])
    print (currAvg)
print (currAvg)
"""
#Try again for a new average
"""
print ("test two")
testValues = [11, 12, 13, 14, 15, 16, 17 , 18 , 19 , 20]
for x in range (0, 10):
    currAvg = pitchAverager(testValues[x])
    print (currAvg)
print (currAvg)
"""

