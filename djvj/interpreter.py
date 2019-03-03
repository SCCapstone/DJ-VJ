#! /usr/bin/env python3
"""
interpreter is the primary decision maker for deciding what video
needs to be played based on the Show.curr_param_values
"""

import operator
from collections import defaultdict


class Interpreter:
    """
    """

    def __init__(self, show):
        self.show = show  # the show Interpreter is interpreting
        self.rules = defaultdict(list)  # the set of rules to interpret by

        self.ops = {
            "<": operator.lt,
            ">": operator.gt,
            "=": operator.eq,
        }

        self.create_rules_table()

    def create_rules_table(self):
        """
        """
        # create map with video paths as key,
        # list of their rule indices as value

        # get indices of video rules
        for index, vid in enumerate(self.show.videos):
            self.rules[vid].append(index)

    # def interpret(self):
    #     """
    #     param based interpreter
    #     """
    #
    #     # main interpreter loop
    #     while True:
    #         # possible videos
    #         possible_videos_index = {}
    #
    #         # for each listening params
    #         for listening_param in self.show.curr_param_values:
    #             # for each rule
    #             for index, param in enumerate(self.show.params):
    #                 # compare current audio param value to show rule value
    #                 # using rule operator
    #                 if self.ops[self.show.operator[index]](self.show.curr_param_values[listening_param], self.show.values[index]):
    #                     possible_videos_index[index] = self.show.videos[index]
    #                     continue
    #                 # otherwise remove index (or do nothing)
    #                 possible_videos_index.pop(index, None)
    #
    #         if len(possible_videos_index) == 1:
    #             _, self.show.curr_video = possible_videos_index.popitem()
    #             print(self.show.curr_video)
    #             continue
    #         print("Show Logic Error")
    #         print(possible_videos_index)

    def interpret(self):
        """
        video based interpreter
        """
        while True:
            found = False
            # for each video in rules
            for video in self.rules:
                # check if video is already the current video being played
                if video != self.show.curr_video:
                    # for each rule for video
                    for index in self.rules[video]:
                        # get what param is being checked
                        index_param = self.show.params[index]
                        # compare current audio param value to show rule value
                        # using rule operator
                        if self.ops[self.show.operator[index]](self.show.curr_param_values[index_param], self.show.values[index]):
                            found = True
                            continue
                        found = False
                        break
                    if found:
                        self.show.curr_video = video
                        break
