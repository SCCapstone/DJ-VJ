#! /usr/bin/env python3

"""
averager.py is used to ensure accurate data is found in the audio
analysis process
"""


class Averager:
    """
    Averager class is used to collect samples of data, remove outliars, and
    find the true current average of data
    """

    def __init__(self):
        self.samples = []  # the list containing the sample set
        self.max_samples = 10  # the number of samples needed to be collected
        self.curr_average = 0  # the current average

    def update_average(self, value):
        """
        update_average
        - takes in the latest found value
        - appends that value to the samples list
        - checks if the samples list is the size of max_samples
        - if the samples list is the size of max_samples, updates the current
        average with find_average(), and emptys the list of samples

        - returns current average
        """

        return self.curr_average


def find_average(samples):
    """
    find_average
    - takes in a list of samples
    - finds the mean of the samples
    - finds the standard deviation of the samples
    - removes the outliars from the list of samples
    - finds the mean of the updated list of samples

    - returns the average

    NOTE:
    - see https://www.kdnuggets.com/2017/02/removing-outliers-standard-deviation-python.html for ideas, it looks like they remove past 2 standard deviations, I think we want to remove
    past 1 standard deviation
    - probably will use numpy module, `import numpy`
    """

    return average
