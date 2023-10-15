#!/usr/bin/python3
"""Operations"""

def minOperations(n):
    """All is well"""
    if (n < 2):
        return 0
    ops, root = 0, 2
    while root <= n:
        # if n evenly divides by root
        if n % root == 0:
            # total even-divisions by root = total operations
            ops += root
            # set n to the remainder
            n = n / root
            # reduce root to find remaining smaller vals that evenly-divide n
            root -= 1
        # increment root until it evenly-divides n
        root += 1
    return ops

if __name__ == "__main__":
    n = 4
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

    n = 9
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
