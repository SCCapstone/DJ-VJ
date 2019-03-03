#! /usr/bin/env python3

"""
"""


class Moment:
    """
    """

    def __init__(self, name, params, operators, values, video):
        self.name = name
        self.params = params  # list of params
        self.operators = operators  # list of operators
        self.values = values  # list of values
        self.video = video  # string of path to video


def create_moments(show_params):
    """
    show_param = list of moments
    moment = ['param', 'operator', value, 'video', 'param', ...]

    returns list of Moments class
    """

    moments = []

    # for each moment in show_params
    for i in range(0, len(show_params)):
        if show_params[i] == []:
            continue
        moment = Moment(("moment" + str(i + 1)), [],
                        [], [], show_params[i][0][3])
        for rule in show_params[i]:
            moment.params.append(rule[0])
            moment.operators.append(rule[1])
            moment.values.append(int(rule[2]))
            if moment.video != rule[3]:
                print("moment video error")
            moment.video = rule[3]

        moments.append(moment)
    return moments
