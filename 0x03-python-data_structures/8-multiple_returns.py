#!/usr/bin/python3
def multiple_returns(sentence):
    """
    Creates tuples with length of input string
    and first character as elements

    Args:
        sentence: input string

    Return: tuple
    """
    return (tuple([len(sentence), sentence[0] if sentence else None]))
