#!/usr/bin/python3
"""this script to define function"""


def minOperations(n):
    """define the function"""
    if n == 1:
        return 0

    operation = 0

    factor = 2
    
    while n > 1:
        while n % factor == 0:
            operation += factor

        n //= factor

        factor += 1

        return operation
