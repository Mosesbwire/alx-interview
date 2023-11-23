# usr/bin/env python3

# 0-making_change.py
import math


import sys

# Utility function for solving the minimum coins problem


def minCoinsUtil(coins, m, V, dp):
    # Base case: If target value V is 0, no coins are needed
    if V == 0:
        return 0

    # If subproblem is already solved, return the result from DP table
    if dp[V] != -1:
        return dp[V]

    res = sys.maxsize

    # Iterate over all coins and recursively solve for subproblems
    for i in range(m):
        if coins[i] <= V:
            # Recursive call to solve for remaining value V - coins[i]
            sub_res = minCoinsUtil(coins, m, V - coins[i], dp)

            # If the subproblem has a valid solution and the total number of coins
            # is smaller than the current result, update the result
            if sub_res != sys.maxsize and sub_res + 1 < res:
                res = sub_res + 1

    # Save the result in the DP table
    dp[V] = res

    return res

# Function to find the minimum number of coins needed to make a target value


def makeChange(coins, total):
    # Create a DP table to store results of subproblems
    dp = [-1] * (total + 1)

    # Call the utility function to solve the problem
    return minCoinsUtil(coins, len(coins), total, dp)


if __name__ == "__main__":
    coins = [1256, 54, 48, 16, 102]
    m = len(coins)
    V = 1453
    res = makeChange(coins, V)

    if res == sys.maxsize:
        res = -1
    # Find the minimum number of coins required
    print("Minimum coins required is", res)
