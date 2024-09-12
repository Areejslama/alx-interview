#!/usr/bin/python3
"""this script to define matrix"""


def rotate_2d_matrix(matrix):
    """define the 2D matrix"""
    n = len(matrix)
    for row in matrix:
        row.reverse()
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
