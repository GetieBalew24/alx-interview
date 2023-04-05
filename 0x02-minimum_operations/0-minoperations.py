#!/usr/bin/python3
'''0x02. Minimum Operations Algorithm Python in a text file
'''


def minOperations(n):
    '''calculates the fewest number of operations needed.
    '''
    total_operation = 0
    total_value = 2
    while n > 1:
        while not n % total_value:
            total_operation += total_value
            n /= total_value
        total_value += 1
    return total_operation