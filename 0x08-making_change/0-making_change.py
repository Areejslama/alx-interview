#!/usr/bin/python3
"""this script to make changes"""


def makeChange(coins, total):
    """define function"""
    if total == 0:
        return 0
    if total < 0:
        return float('inf')
    if len(coins) == 0:
         return float('inf')
    return min(makeChange(coins[1:], total),
            makeChange(coins, total - coins[0]) + 1)
