#!/usr/bin/python3
"""this script to make changes"""


def makeChange(coins, total):
    """define function"""
    if coins is None:
        return -1
    if total <= 0:
        return 0
    change = 0
    coins = sorted(coins, reverse=True)

    i = 0
    while total > 0 and i < len(coins):
        coin = coins[i]
        while coin <= total:
            total -= coin
            change += 1
        i += 1

    if total == 0:
        return change
    else:
        return -1
