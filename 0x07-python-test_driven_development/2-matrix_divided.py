#!/usr/bin/python3
"""Function that performs a scalar division"""


def matrix_divided(matrix, div):
    """ This performs a scalar division on every element of a matrix

    Args:
        matrix: a list of list of rational Numbers
        div: integer dividor
    Returns:
        list: A new matrix resulting from the division.

    Raises:
        TypeError: If the input matrix is not a valid list of lists of integers/floats
                   or if the divisor is not a number.
        ZeroDivisionError: If attempting to divide by zero.
    """
    if any(type(row) != list for row in matrix):
        raise TypeError("matrix must be a matrix"
                        "(list of lists) of integers/floats")
    for row in matrix:
        if any(not isinstance(el, (int, float)) for el in row):
            raise TypeError("matrix must be a matrix"
                            "(list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix[1:]):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    try:
        new_matrix = [[round(a / div, 2) for a in row] for row in matrix]
    except ZeroDivisionError:
        raise ZeroDivisionError("division by zero")
    else:
        return new_matrix
