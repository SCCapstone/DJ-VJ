from math import log2

class PitchAvgs:
	def __init__(self, pitch):
	    self.pitch = pitch
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
        tenInt = sum(self.pitchArr)
        average = tenInt / 10
        self.lastAvg = average
        return average
    elif length < 10:
        if length == 0:
            return 0
        else:
            return self.lastAvg