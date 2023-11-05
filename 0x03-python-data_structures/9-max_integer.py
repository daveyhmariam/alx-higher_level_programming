#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    Finds the maximimum in a list

    Args:
        my_list: list to be evaluated

    Return: None if list is empty, max value
    """
    if not my_list:
        return None
    my_list.sort()
    return my_list[-1]
