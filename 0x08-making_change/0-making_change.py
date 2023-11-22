#!/usr/bin/python3
"""Making some change for market day"""


def makeChange(coins, total):
    """Make change challenge"""
    if total <= 0:
        return 0

    sum = 0
    count = 0
    change = list(reversed(sorted(coins)))
    # print(change)
    for coin in change:
        while sum + coin <= total:
            count = count + 1
            sum = sum + coin
        # print(f"{coin} {count} {sum} {total}")
        if sum == total:
            return count
    return -1
