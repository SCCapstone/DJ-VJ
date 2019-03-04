"""
The imports I had when it was in the test folder
import djvj.pitchAverager as pitchAverager
from djvj.pitchAverager import pitchAverager
from djvj.pitchAverager import PitchAvgs
"""
from Averager import Averager
from Averager import Avgs
import unittest


"""
Testing the pitchAverager function
"""
"""
Old Unit Test for finding the actual average

class TestPitchAvgs(unittest.TestCase):
    
    def test_avgsmethod(self):
        self = PitchAvgs(1)
        self.valArr.append(self.pitch)
        for x in range (1, 10):
            self.valArr.append(x)	
        self.lastAvg = pitchAverager(self)
        print(self.lastAvg)

if __name__ == '__main__':
    unittest.main()
"""

#Test 1 test if it will find the mode after 10 numbers are placed in the valArr
print ("test 1")
testValues = [10, 10, 3, 15, 15, 10, 10 , 11 , 9 , 10]
pitch1 = Avgs()
for x in range (0, 10):
    pitch1.valArr.append(testValues[x])
    print (pitch1.lastAvg)
currAvg = Averager(pitch1)
print (pitch1.lastAvg)
print (currAvg)

#Test 2 tries again for a new average and makes sure the old list clears

print ("test two")
testValues2 = [10, 12, 3, 15, 15, 12, 12 , 11 , 9 , 12]
for x in range (0, 10):
    pitch1.valArr.append(testValues2[x])
    print (pitch1.lastAvg)
currAvg = Averager(pitch1)
print (pitch1.lastAvg)
print (currAvg)
"""
Test 3 Checks that it will still hold the values in the list even tho it hasn't
reached a length of 10 yet and still outputs the last Mode it found
"""
print("test 3")
testValues3 = [5, 13, 13, 7, 10, 13, 11, 45]
for x in range (0, 8):
    pitch1.valArr.append(testValues3[x])
    print (pitch1.lastAvg)
currAvg = Averager(pitch1)
print (pitch1.lastAvg)
print (currAvg)
"""
Test 4 makes sure that it still finds the Mode once we start putting new numbers 
into the list
"""
print("test4")
testValues4 = [5, 13, 13, 7, 10, 13, 11, 45, 13, 69, 40]
for x in range (0, 8):
    pitch1.valArr.append(testValues4[x])
    currAvg = Averager(pitch1)
    print (pitch1.lastAvg)
currAvg = Averager(pitch1)
print (pitch1.lastAvg)
print (currAvg)
