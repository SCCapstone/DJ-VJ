from math import log2
from collections import Counter

class PitchAvgs:
	def __init__(self):
	    self.pitch = 0
	    self.pitchArr = []
	    #self.pitchArr.append(pitch)
	    self.lastAvg = 0

def pitchAverager(self):
    """
    Takes in pitch values, stores them, and once it reaches a certain number 
    of pitch values, takes the average and returns the average.
    """
    #arr1.append(self)
    #Gets the length of the Array
    length = len(self.pitchArr)
    
    if length == 10:
        average = Counter(self.pitchArr)
        self.lastAvg = average.most_common(1)
        self.pitchArr.clear()
        return self.lastAvg
    elif length < 10:
        if length == 0:
            return self.lastAvg
        else:
            self.pitchArr.clear()
            return self.lastAvg