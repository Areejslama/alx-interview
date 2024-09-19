#!/usr/bin/python3
"""this script to make changes"""


def makeChange(coins, total):
    """define function"""
    if total == 0:
        return 0
    if total < 0:
        return 0
    if len(coins) == 0:
        return -1
    use_coin = makeChange(coins, total - coins[0])
    skip_coin = makeChange(coins[1:], total)
    return min(use_coin + 1, skip_coin)

