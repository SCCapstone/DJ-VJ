from math import log2


def pitchAverager(self):
    """
    Takes in pitch values, stores them, and once it reaches a certain number 
    of pitch values, takes the average and returns the average.

    Does the array need to be global? will I lose the array every time this function is called?
    """
    arr1 = []
    arr1.append(self)
    length = len(arr1)
    
    if length == 10:
        tenInt = sum(arr1)
        average = tenInt / 10
        arr1 = []
        return average
    elif length < 10:
        if length == 0:
            return 0
        else:
            return 0