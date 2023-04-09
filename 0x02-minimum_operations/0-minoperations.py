#!/usr/bin/python3
'''Minimum Operations Algorithm in python'''


def minOperations(n):
    '''calculates number operations '''
    total_operation = 0
    # all outputs have at least 2 letters
    for root_value in range(2, n+1):
        # if n modules by root_value
        while not n % root_value:
            # add total_operation and root_value
            total_operation += root_value
            # set n to the value of remainder
            n /= root_value
        # if n equal to 1 terminate the while
        if n == 1:
            break
    # return total number of operations
    return total_operation