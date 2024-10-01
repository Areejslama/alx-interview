#!/usr/bin/python3
"""this script to define method"""


def isWinner(x, nums):
    """Determine the winner of the game for x rounds."""
    if x <= 0 or not nums:
        return None
    max_nums = max(nums)
    prime = [True for i in range(max_nums + 1)]
    prime[0], prime[1] = False, False
    p = 2
    while (p * p <= max_nums):
        if prime[p]:
            for i in range(p * p, max_nums + 1, p):
                prime[i] = False
        p += 1
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        count = sum(prime[2:n+1])
        if count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
