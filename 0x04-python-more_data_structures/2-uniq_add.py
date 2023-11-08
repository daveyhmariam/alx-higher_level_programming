#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Summes up unique elements of a list

    Args:
        my_list: input list

    Return: the result
    """
    set1 = set(my_list)
    sum = 0
    for i in set1:
        sum += i
    return sum
