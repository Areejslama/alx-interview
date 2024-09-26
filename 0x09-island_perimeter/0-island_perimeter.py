#!/usr/bin/python3
"""this script define method"""


def island_perimeter(grid):
    """define function"""
    pri = 0;

    m = len(grid)
    n = len(grid[0])

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                if j == 0 or grid[i][j - 1] == 0:
                    pri += 1
                if j == n - 1 or grid[i][j + 1] == 0:
                    pri += 1
                if i == 0 or grid[i - 1][j] == 0:
                    pri += 1
                if i == m - 1 or grid[i + 1][j]:
                    pri += 1
    return pri

