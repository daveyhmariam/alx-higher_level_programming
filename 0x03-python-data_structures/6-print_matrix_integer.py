#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):

    for r in matrix:
        for cl in r:
            print("{:d}{}".format(cl, "" if cl == r[-1] else " " ), end="")
        print("")
