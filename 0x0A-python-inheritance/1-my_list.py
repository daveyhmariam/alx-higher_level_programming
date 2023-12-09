#!/usr/bin/python3
"""Inherited class from list class"""


class MyList(list):
    """MyList inherits from list and prints sorted list"""
    def __init__(self):
        """
        Inherits list and adds a method print_sorted that
        """
    def print_sorted(self):
        """
        Prints a sorted version of the class's instance
        """
        print(sorted(self))
