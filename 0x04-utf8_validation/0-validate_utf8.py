#!/usr/bin/python3
""" UTF-8 Validation 
that determines if a given data set
represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Checks if a list of integers are valid UTF-8 codepoints.
    """
    count_bytes = 0

    bit1 = 1 << 7
    bit2 = 1 << 6

    for i in data:

        cont_byte = 1 << 7

        if count_bytes == 0:

            while cont_byte & i:
                count_bytes += 1
                cont_byte = cont_byte >> 1

            if count_bytes == 0:
                continue

            if count_bytes == 1 or count_bytes > 4:
                return False

        else:
            if not (i & bit1 and not (i & bit2)):
                    return False

        count_bytes -= 1

    if count_bytes == 0:
        return True

    return False