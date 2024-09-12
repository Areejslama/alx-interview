#!/usr/bin/python3
"""this script to define matrix"""


def rotate_2d_matrix(matrix):
    """define the 2D matrix"""
    n = len(matrix)
    for layer in range(n // 2):
        first, last = layer, n - layer - 1

        for i in range(first, last):
            # offset keeps track of how far the element is from the 'first'
            offset = i - first
            
            # Save the top element
            top = matrix[first][i]
            
            # Move left to top
            matrix[first][i] = matrix[last - offset][first]
            
            # Move bottom to left
            matrix[last - offset][first] = matrix[last][last - offset]
            
            # Move right to bottom
            matrix[last][last - offset] = matrix[i][last]
            
            # Move top to right
            matrix[i][last] = top
