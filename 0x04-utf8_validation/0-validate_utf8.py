#!/usr/bin/python3
"""UTF-8 validationa method that determines 
if a given data set represents a valid UTF-8 encoding .
"""


def validUTF8(data):
    """Checks if a list of integers are valid UTF-8 codepoints.
    """
    cont_byte = 0
    count = len(data)
    for i in range(count):
        if cont_byte > 0:
            cont_byte -= 1
            continue
        if (type(data[i]) != int or data[i] < 0 or data[i] > 0x10ffff):
            return False
        elif (data[i] <= 0x7f):
            cont_byte = 0
        elif (data[i] & (0b11111000 == 0b11110000)):
            """4-byte utf-8 character encoding"""
            cont_span = 4
            if (count - i >= cont_span):
                next_byte = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + cont_span],
                ))
                if (not all(next_byte)):
                    return False
                cont_byte = cont_span - 1
            else:
                return False
        elif (data[i] & (0b11110000 == 0b11100000)):
            """3-byte utf-8 character encoding"""
            cont_span = 3
            if (count - i >= cont_span):
                next_byte = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + cont_span],
                ))
                if (not all(next_byte)):
                    return False
                cont_byte = cont_span - 1
            else:
                return False
        elif (data[i] & 0b11100000 == 0b11000000):
            """2-byte utf-8 character encoding"""
            span = 2
            if (count - i >= span):
                next_byte = list(map(
                    lambda x: x & 0b11000000 == 0b10000000,
                    data[i + 1: i + span],
                ))
                if (not all(next_byte)):
                    return False
                cont_byte = cont_span - 1
            else:
                return False
        else:
            return False
    return True