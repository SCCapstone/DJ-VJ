from math import log2
from djvj.Averager import Averager
from djvj.Averager import Avgs
import unittest


"""
Testing the pitchAverager function
"""
class TestPitchAvgs(unittest.TestCase):
    
    def test_avgsmethod(self):
        self = Avgs()
        testVals = [10, 10, 3, 15, 15, 10, 10 , 11 , 9 , 10]
        for x in range (0, 10):
            self.valArr.append(testVals[x])	
        currAvg = Averager(self)
        print(currAvg)

        testVals2 = [10, 12, 3, 15, 15, 12, 12 , 11 , 9 , 12]
        for x in range (0, 10):
            self.valArr.append(testVals2[x])
        currAvg = Averager(self)
        print(currAvg)

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

