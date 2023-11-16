#!/usr/bin/python3
"""This is the code"""


def rotate_2d_matrix(matrix):
    """Rotates a 2d matrix"""
    n = len(matrix)
    copy = [x.copy() for x in matrix]
    for i in range(n):
        for j in range(n):
            matrix[i][j] = copy[j][i]
        matrix[i] = list(reversed(matrix[i]))
