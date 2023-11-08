#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    updates dictionary with key-value pair

    Args:
        a_dictioary: input dictionary
        key: key for dict
        value: value for the key
    """
    a_dictionary.update({key: value})
    return a_dictionary
