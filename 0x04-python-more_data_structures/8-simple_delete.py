#!/usr/bin/pytho3
def simple_delete(a_dictionary, key=""):
    """
    Delete a specific key

    Args:
        a_dictionary: input dict object
        key: key to be deleted
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
