#!/usr/bin/python3
def multiple_returns(sentence):
    """
    Creates tuples with length of input string
    and first character as elements

    Args:
        sentence: input string

    Return: tuple
    """
    if sentence:
        return (tuple([len(sentence), sentence[0]]))
