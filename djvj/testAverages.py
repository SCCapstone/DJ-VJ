from math import log2
from pitchAverager import pitchAverager
from pitchAverager import PitchAvgs
import unittest


"""
Testing the pitchAverager function
"""

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
testValues = [10, 10, 3, 15, 15, 10, 10 , 11 , 9 , 10]
pitch1 = PitchAvgs()
for x in range (0, 10):
    pitch1.pitchArr.append(testValues[x])
    print (pitch1.lastAvg)
currAvg = pitchAverager(pitch1)
print (pitch1.lastAvg)
print (currAvg)

#Try again for a new average

print ("test two")
testValues2 = [10, 12, 3, 15, 15, 12, 12 , 11 , 9 , 12]
for x in range (0, 10):
    pitch1.pitchArr.append(testValues2[x])
    print (pitch1.lastAvg)
currAvg = pitchAverager(pitch1)
print (pitch1.lastAvg)
print (currAvg)
