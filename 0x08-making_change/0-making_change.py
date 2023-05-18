#!/usr/bin/python3
""" Contains makeChange function"""


def makeChange(coins, total):
    """
    Returns: fewest number of coins needed to meet total
        If total is 0 or less, return 0
        If total cannot be met by any number of coins you have, return -1
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    var_change = 0
    coins = sorted(coins)[::-1]
    for con in coins:
        while con <= total:
            total -= con
            var_change += 1
        if (total == 0):
            return var_change
    return -1