#!/usr/bin/python3
""" Prime game """


def sqrt(n):
    """returns square root of n"""
    for i in range(1, n):
        if i * i > n:
            return i - 1
        if i * i == n:
            return i
    return 0


def generate_primes(n: int) -> list[int]:
    """generate prime numbers between 0 and n"""
    isPrime = [True for i in range(n + 1)]
    isPrime[0] = False
    isPrime[1] = False

    for i in range(2, sqrt(n)):
        if isPrime[i]:
            j = i * i
            while j <= n:
                isPrime[j] = False
                j += i
    primes = []

    for i in range(len(isPrime)):
        if isPrime[i]:
            primes.append(i)
    return primes


def isWinner(x: int, nums: list[int]):
    """ return winner after x number of rounds played """
    score_board = {"miriam": 0, "ben": 0}
    if x > len(nums):
        return None
    primes = generate_primes(max(nums))
    for i in range(x):
        if len(primes) == 0:
            score_board["ben"] = score_board["ben"] + 1
        elif len(primes) % 2 == 0:
            score_board["ben"] = score_board["ben"] + 1
        else:
            score_board["miriam"] = score_board["miriam"] + 1
    if score_board["ben"] > score_board["miriam"]:
        return "Ben"
    if score_board["miriam"] > score_board["ben"]:
        return "Miriam"
    return None
