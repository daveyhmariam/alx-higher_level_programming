#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    val = list(a_dictionary.values())
    val.sort()
    max = val.pop()
    for keys in a_dictionary:
        if a_dictionary[keys] == max:
            return keys
