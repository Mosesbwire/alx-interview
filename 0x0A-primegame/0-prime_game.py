#!/usr/bin/python3

"""Module 0-prime_game
Algorithm generates primes numbers and select winner based on number of rounds played and number of primes
"""


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
    if n < 2:
        return []
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False

    for i in range(2, sqrt(n) + 1):
        if is_prime[i]:
            j = i * i
            while j <= n:
                is_prime[j] = False
                j += i
    primes = [i for i in range(n + 1) if is_prime[i]]
    return primes


def isWinner(x: int, nums: list[int]):
    """return winner after x number of rounds played"""
    score_board = {"miriam": 0, "ben": 0}
    if x > len(nums) or not nums:
        return None
    for i in range(x):
        primes = generate_primes(nums[i])
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
