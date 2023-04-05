#!/usr/bin/python3
'''Minimum Operations Algorithm in python '''


def minOperations(n):
    if n == 1:
        return 0
    count = 0
    numH = 1
    while numH < n:
        if n % numH == 0:
            count += n // numH - 1
            numH = n // (n // numH)
        else:
            numH *= 2
            count += 1
    return count if numH == n else 0