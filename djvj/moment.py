#! /usr/bin/env python3
"""
moment.py is used to convert the GUI list of moments to a list of Moments

__author__ = "Matthew J. Smith"
__email__ = "mjs10@email.sc.edu"
"""


class Moment:
    """
    Moment class sets up an instance of a Moment
    """

    def __init__(self, name, params, operators, values, video):
        self.name = name
        self.params = params  # list of params
        self.operators = operators  # list of operators
        self.values = values  # list of values
        self.video = video  # string of path to video


def create_moments(show_params):
    """
    create_moments converts the GUI list of moments to a list of Moments

    show_param = list of moments
    moment = ['param', 'operator', value, 'video', 'param', ...]

    returns list of Moments class
    """

    # list of Moments
    moments = []

    # for each moment in show_params
    for i, _ in enumerate(show_params):
        # if empty list, skip
        if show_params[i] == []:
            continue
        # instantiate Moment
        moment = Moment(("moment" + str(i + 1)), [],
                        [], [], show_params[i][0][3])
        # for each rule in a moment
        for rule in show_params[i]:
            moment.params.append(rule[0])  # add the param
            moment.operators.append(rule[1])  # add the operator
            moment.values.append(int(rule[2]))  # add the value

            # check if vide in each rule are the same
            if moment.video != rule[3]:
                print("moment video error")
            moment.video = rule[3]  # add the video
        # print(vars(moment))

        # add Moment to list of Moments
        moments.append(moment)
    return moments
