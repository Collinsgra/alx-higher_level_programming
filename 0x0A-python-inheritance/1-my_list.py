#!/usr/bin/python3
"""
contains classes
"""


class MyList(list):
    """ subclass """

    def __init__(self):
        """initialize_object"""
        super().__init__()

    def print_sorted(self):
        """prints slist"""
        print(sorted(self))
