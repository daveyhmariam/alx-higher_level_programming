#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """This class inherits from the rectangle class

    Args:
        Rectangle (class): rectangle class that is subclass of the base class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Initializer of instance object

        Args:
            size (int): length of square
            x (int, optional): x coordinate. Defaults to 0.
            y (int, optional): y coordinate. Defaults to 0.
            id (_type_, optional): object id. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation of instance object
        """
        return ("[Square] ({}) {}/{} - {}"
                "".format(self.id, self.x,
                          self.y, self.width))
