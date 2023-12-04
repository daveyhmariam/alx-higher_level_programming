#!/usr/bin/python3
"""Inherited class from list class"""


class MyList(list):
    """MyList inherits from list and prints sorted list"""

    def print_sorted(self):
        print(sorted(self))
