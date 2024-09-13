#!/usr/bin/python3
"""this script to define function"""



def pascal_triangle(n):
    """Generate Pascal's Triangle up to n rows."""
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        for num in range(1, i):
            row.append(triangle[i - 1][num - 1] + triangle[i - 1][num])
        row.append(1)
        triangle.append(row)

    return triangle
