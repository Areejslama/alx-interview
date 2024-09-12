#!/usr/bin/python3
"""this script to define matrix"""


def rotate_2d_matrix(matrix):
    """define the 2D matrix"""
    N = len(matrix)
    for layer in range(n // 2):
        first, last = layer, n - layer - 1

        for i in range(first, last):
            # offset keeps track of how far the element is from the 'first'
            offset = i - first
            
            # Save the top element
            top = mat[first][i]
            
            # Move left to top
            mat[first][i] = mat[last - offset][first]
            
            # Move bottom to left
            mat[last - offset][first] = mat[last][last - offset]
            
            # Move right to bottom
            mat[last][last - offset] = mat[i][last]
            
            # Move top to right
            mat[i][last] = top
