#!/usr/bin/;python3
def new_in_list(my_list, idx, element):
    """

    Non side-effect function

    Args:
       my_list: list
       idx: index at which elemet is to be changed
       element: item to replace

    Returns: a copy of the input list
    """
    if my_list:
        if idx < 0 or idx >= len(my_list):
            return (my_list)
        new_list = my_list.copy()
        new_list[idx] = element
        return (new_list)
