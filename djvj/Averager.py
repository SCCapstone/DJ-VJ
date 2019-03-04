#! /usr/bin/env python3

"""
Defines the Averager class that can store an individual value,
a list of values, and the last average that was calculated by the
Averager function
"""
from collections import Counter

class Avgs:
    def __init__(self):
        self.val = 0
        self.valArr = []
	    #self.pitchArr.append(pitch)
        self.lastAvg = 0

def Averager(self):
    """
    Takes in values, stores them, and once it reaches a certain number
    of values(in this case 10) it finds the mode out of the list
    and returns that mode.
    """
    gets_tuple = 0
    #Gets the length of the Array
    length = len(self.valArr)
    if length == 10:
        average = Counter(self.valArr)
        gets_tuple = average.most_common(1)
        self.lastAvg = gets_tuple[0][0]
        self.valArr.clear()
        return self.lastAvg
    elif length > 10:
        self.valArr.clear()
        return self.lastAvg
    else:
        return self.lastAvg
