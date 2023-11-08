#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    print a sorted key dictionary

        Args:
        a_dictionary: input dictionary
    Return: None
    """
    key_list = list((a_dictionary.keys()))
    key_list.sort()
    for k in key_list:
        print(f"{k}: {a_dictionary[k]}")
