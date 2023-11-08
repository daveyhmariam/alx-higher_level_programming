#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Calculate the square of list elements

    Args:
        matrix: two dimentional list

    Return: new marix
    """
    new_matrix = [list(map(lambda x: x**2, r)) for r in matrix]
    return new_matrix
