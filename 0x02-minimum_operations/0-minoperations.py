#!/usr/bin/python3
""" Module for 0-minoperationsIn a text file.
"""


def minOperations(n):
    """ methods to calculate the fewest number of operations
    """

    # all outputs should be at least 2 char: (min, Copy All => Paste)
    if (n < 2):
        return 0
    total_operation, root_value = 0, 2
    while root_value <= n:

        # if n modules root_value
        if n % root_value == 0:

            # the sum of total operation and root_value = total operations
            total_operation += root_value

            # set n to n divided by the root_value
            n = n / root_value

            # substract root_value by one to find the smaller values 
            root_value -= 1

        # increment root_value by one until it divides n
        root_value += 1

    return total_operation
