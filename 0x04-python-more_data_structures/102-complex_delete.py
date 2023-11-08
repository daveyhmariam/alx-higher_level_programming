#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if not a_dictionary:
        return a_dictionary
    val_list = list(a_dictionary.values())
    if value not in val_list:
        return a_dictionary
    for keys in list(a_dictionary.keys()):
        if value == a_dictionary[keys]:
            del a_dictionary[keys]
    return a_dictionary
