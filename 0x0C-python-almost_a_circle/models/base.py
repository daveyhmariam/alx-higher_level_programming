#!/usr/bin/python3
"""Base class for subsequent geometric classes"""

class Base:
    """Base class for all geometric ssubclasses
    """
    __nb_objects = 0
    
    def __init__(self, id=None):
        """Object initializer

        Args:
            id (int, optional): id number. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
