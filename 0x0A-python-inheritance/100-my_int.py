#!/usr/bin/python3
"""MyInt class that inherits from int"""


class MyInt(int):
    """This class inherits from int and inverts the operators == and !="""

    def __eq__(self, other):
        """invert the logical equal operator

        Args:
            other (object):
        Return: self != other
        """
        return not super().__eq__(other)

    def __ne__(self, other):
        """invert the logical not equal operator

        Args:
            other (object):
        Return: self == other
        """
        return not super().__ne__(other)
