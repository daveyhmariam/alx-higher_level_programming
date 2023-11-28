#!/usr/bin/python3
"""
The code is importing the `argv`
variable from the `sys` module,
which allows the script to access
command-line arguments.
"""
import sys


def board(N):
    """Creates new board

    Args:
        N (int): size of board

    Returns:
        list of list
    """
    return [[0 for col in range(N)] for row in range(N)]


def solution(col=0):
    """
    Finds all solutions for N queen problem using backtracking

    Args:
        col (int): the column to be recursively calculated
    """
    global new_board
    if col == N:
        return
    for row in range(N):
        if row in Q or (row+col) in Qu or (row-col) in Qd:
            continue
        Q.add(row)
        Qu.add(row+col)
        Qd.add(row-col)
        new_board[row][col] = 1
        if col == (N-1):
            get_solution(new_board)
        solution(col+1)
        new_board[row][col] = 0
        Q.remove(row)
        Qu.remove(row+col)
        Qd.remove(row-col)
    return


def get_solution(brd):
    """
    Gets the indecies of the possible solutios from the board

    Args:
        brd (board): the board state on the possible solution
    """
    global sol
    indx = []
    for i in range(N):
        for j in range(N):
            if brd[i][j] == 1:
                indx.append([i, j])
    sol.append(indx)


if __name__ == '__main__':
    """Starting of execution of program
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    N = int(sys.argv[1])
    if not isinstance(N, int):
        print("N must be a number")
        exit(1)
    if N < 4:
        print("N must be at least 4")
    new_board = board(N)
    sol = []
    Q = set()
    Qu = set()
    Qd = set()
    solution(0)
    for s in sol:
        print(s)
