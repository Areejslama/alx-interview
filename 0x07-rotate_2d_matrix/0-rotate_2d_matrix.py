#!/usr/bin/python3
"""this script to define matrix"""


def rotate_2d_matrix(matrix):
    """define the 2D matrix"""
    n = len(matrix)
    for layer in range(n // 2):
        first, last = layer, n - layer - 1

        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]
            matrix[first][i] = matrix[last - offset][first]
            matrix[last - offset][first] = matrix[last][last - offset]
            matrix[last][last - offset] = matrix[i][last]
            matrix[i][last] = top
