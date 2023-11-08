#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    if not matrix:
        return matrix
    new_matrix = list(map(lambda y: list(map(lambda x: x ** 2, y)), matrix))
    return new_matrix