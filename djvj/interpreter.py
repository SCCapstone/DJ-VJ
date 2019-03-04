#! /usr/bin/env python3
"""
interpreter is the primary decision maker for deciding what video
needs to be played based on the Show.curr_param_values

__author__ = "Matthew J. Smith"
__email__ = "mjs10@email.sc.edu"
"""

import operator
import time


class Interpreter:
    """
    Interpreter class sets up an instance of an Interpreter

    requires a Show class
    """

    def __init__(self, show):
        self.show = show  # the show Interpreter is interpreting
        self.sleep = .1  # sleep in between current video updates

        # dictionary to used to convert string operators to actual operators
        self.ops = {
            "<": operator.le,
            ">": operator.gt,
            "=": operator.eq,
        }

    def interpret(self):
        """
        interpreter compares the current parameter values to the values
        in each Show.Moment to see if they match
        If it finds a match, then updates the Show current video
        If it does not find a match, then the show was not created correctly

        requires each Moment to only have one video
        """
        # main interpreter loop
        while True:
            # possible moments
            possible_moments = {}
            # for each moment
            for moment in self.show.moments:
                # check if moment video is already the current video being played
                # if so, no need to interpret
                if moment.video == self.show.curr_video:
                    print("skip")
                    continue
                # for each param in a moment
                for index, param in enumerate(moment.params):
                    print(moment.name, param, moment.values[index])
                    print(self.show.curr_param_values)
                    # get current value of param
                    curr_param_value = self.show.curr_param_values[param]
                    # get value of moment param
                    moment_param_value = moment.values[index]
                    print(self.ops[moment.operators[index]](
                        curr_param_value, moment_param_value))
                    # compare current param value to show rule value
                    # using rule operator
                    # if true, add to possible values and continue to next moment param
                    if self.ops[moment.operators[index]](curr_param_value, moment_param_value):
                        possible_moments[moment] = [moment.name, param]
                        continue
                    # otherwise remove moment (or do nothing)
                    possible_moments.pop(moment, None)
                    # break to next moment
                    break
            # check if more than one possible moments
            # if so, show was not created correctly
            if len(possible_moments) != 1:
                print("Show Logic Error")
                for moment in possible_moments:
                    print(moment.name)
                time.sleep(self.sleep)
                continue
            # get moment that was found to match current audio values
            print("clear")
            moment, _ = possible_moments.popitem()
            # update the show current video
            self.show.curr_video = moment.video
            # delay next interpret to save processing power
            time.sleep(self.sleep)
