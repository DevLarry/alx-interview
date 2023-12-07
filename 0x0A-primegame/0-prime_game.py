#!/usr/bin/python3
"""Prime game"""


def isPrime(num):
    """Checks if a number is prime"""
    if num > 1:
        # Iterate from 2 to n / 2
        for i in range(2, int(num/2)+1):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False


def firstPrime(nums):
    """Finds the first prime number in a list"""
    for num in nums:
        if isPrime(num):
            return num
    return None


def isWinner(x, nums):
    """Checks whether the current player wins the game"""
    # won = False
    rounds = 0
    wins = []
    while(rounds < x):
        isMaria = True
        n = nums[rounds]
        nset = [i for i in range(1, n + 1)]
        choice = firstPrime(nset)
        if choice is None:
            wins.append(not isMaria)
        while(choice is not None):
            nset = [i for i in nset if i % choice != 0]
            choice = firstPrime(nset)
            if choice is None:
                wins.append(isMaria)
                isMaria = True
                break
            isMaria = not isMaria
        rounds += 1
    maria = 0
    ben = 0
    # if len(wins) == 0:
    #     return None
    for win in wins:
        if win is True:
            maria += 1
        else:
            ben += 1
    if ben > maria:
        return "Ben"
    elif ben < maria:
        return "Maria"
    else:
        return None


if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
