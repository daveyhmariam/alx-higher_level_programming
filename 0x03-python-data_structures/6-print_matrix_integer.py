#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    Print elements or matrix in order

    Args:
        matrix: input matrix
    Return: None
    """
    for r in matrix:
        for cl in r:
            print("{:d}".format(cl), end=" ")
        print("")
