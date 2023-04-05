#!/usr/bin/python3
''' Minimum Operations Algorithm in python '''


def minOperations(n):
    ''' calculates number operations '''
    # all outputs have at least 2 letters
    total_operation = 0
    root_value = 2
    while n > 1:
        # if n modules by root_value
        while not n % root_value:
            # add total_operation and root_value
            total_operation += root_value
            # set n to the valoe of remainder
            n /= root_value
        # increment root by one until n lessthan 0
        root_value += 1
    return total_operation