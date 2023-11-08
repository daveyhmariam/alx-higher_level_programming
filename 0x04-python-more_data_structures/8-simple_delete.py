#!/usr/bin/pytho3
def simple_delete(a_dictionary, key=""):
    """
    Delete a specific key

    Args:
        a_dictionary: input dict object
        key: key to be deleted
    """
    if key:
        if key in list(a_dictionary.keys()):
            del a_dictionary[key]
            return a_dictionary
        return a_dictionary
