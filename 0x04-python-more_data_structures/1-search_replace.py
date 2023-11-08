#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Replace an element of list elegantly

    Args:
        my_list: input list
        search: the element to be replaced
        replace: replacing element
    Return: a new modified list
    """
    new = list(map(lambda x: replace if x == search else x, my_list))
    return new
