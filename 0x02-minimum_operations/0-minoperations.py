#!/usr/bin/python3
''' Minimum Operations Algorithm in python '''


def minOperations(n):
    ''' calculates number operations '''
    # all outputs have at least 2 letters
    total_operation = 0
    for root_value in range(2, n+1):
        # if n modules by root_value
        while not n % root_value:
            # add total_operation and root_value
            total_operation += root_value
            # set n to the value of remainder
            n /= root_value
        if n == 1:
            break
    return total_operation