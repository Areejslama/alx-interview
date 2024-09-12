#!/usr/bin/python3
"""this script to define matrix"""


def rotate_2d_matrix(matrix):
    """define the 2D matrix"""
    N = len(matrix)  # Get the size of the matrix dynamically

    # Consider all squares one by one
    for x in range(0, N // 2):
        
        # Consider elements in groups of 4 in the current square
        for y in range(x, N - x - 1):
            
            # Store the current cell in a temporary variable
            temp = matrix[x][y]

            # Move values from right to top
            matrix[x][y] = matrix[y][N - 1 - x]

            # Move values from bottom to right
            matrix[y][N - 1 - x] = matrix[N - 1 - x][N - 1 - y]

            # Move values from left to bottom
            matrix[N - 1 - x][N - 1 - y] = matrix[N - 1 - y][x]

            # Assign the temp to the left
            matrix[N - 1 - y][x] = temp
