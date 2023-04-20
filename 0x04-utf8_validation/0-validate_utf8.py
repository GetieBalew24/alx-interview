#!/usr/bin/python3
""" a method that determines 
if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """ Counter of the number of expected continuation bytes
    """
    cont_bytes = 0
    
    for byte in data:
        """Check if the byte is a continuation byte"""
        if cont_bytes > 0 and (byte >> 6) == 0b10:
            cont_bytes -= 1
            """Check if the byte is a leading byte"""
        elif cont_bytes == 0:
            """Count the number of leading 1 bits"""
            bit = 0b10000000
            while bit & byte:
                cont_bytes += 1
                bit >>= 1
            """Handle invalid cases"""
            if cont_bytes == 1 or cont_bytes > 4:
                return False
            """ Handle invalid cases"""
        else:
            return False
    
    """ If all bytes have been processed, 
    the encoding is valid"""
    return cont_bytes == 0