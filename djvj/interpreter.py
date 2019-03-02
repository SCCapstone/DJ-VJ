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
        # map: [video]: rule

        # get indices of video rules
        for index, vid in enumerate(self.show.videos):
            self.rules[vid].append(index)

    def interpret(self):
        """
        """
        while True:
            found = False
            # for each video in rules
            for video in self.rules:
                # for each rule for video
                for index in self.rules[video]:
                    index_param = self.show.params[index]
                    if self.ops[self.show.operator[index]](self.show.curr_param_values[index_param], self.show.values[index]):
                        found = True
                        continue
                    found = False
                    break
                if found:
                    self.show.curr_video = video
                    break
