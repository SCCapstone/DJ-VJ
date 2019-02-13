#! /usr/bin/env python3

"""
interpreter is the main file for deciding which videos to play at given moment
of time
"""


class Interpreter:
    """
    Interpreter is the class where the show_dictionary is created which is used
    as the rule set to compare to a given set of curr_audio values
    """

    def __init__(self, show_params):
        """
        show_params = [[params], [rules], [values], [videos]]
        """
        self.params = show_params[0]  # pitch, tempo, etc
        self.rules = show_params[1]  # <, =, etc
        self.values = show_params[2]  # 500, 120, etc
        self.videos = show_params[3]  # video_paths

        """
        show_dictionary = {
            key: value
        }
        -key is an identifier (type string)
        -value is the video_path (type string)
        """
        self.show_dictionary = {}

        """
        curr_video is the path to the current video that is playing as a string
        """
        self.curr_video = ""

    def create_show_dictionary(self):
        """
        create_show_dictionary
        uses the interpreter's show_params to populate the show_dictionary
        """

        # updates self.show_dictionary, does not need to return

    def make_decision(self, curr_values):
        """
        make_decision
        - takes in a set of current values
        curr_values = curr_param_values = {
            'pitch': <curr_value>,
            'tempo': <curr_value>,
            'volume': <curr_value>.
            'time:' <curr_value>
        }
        - creates an identifier based on those values
        - compares that identifier to the identifiers found in
        self.show_dictionary, make sure only to check the ones that are being listened for
        - decides if self.curr_video needs to be updated
        """

        # updates self.curr_video, does not need to return
