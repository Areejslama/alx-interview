#!/usr/bin/python3
"""This script defines a function to calculate the fewest number of operations"""


def minOperations(n):
    """Define the function to calculate minimum operations."""
    operation = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operation += factor
            n //= factor
        factor += 1

    return operation
