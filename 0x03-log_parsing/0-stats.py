#!/usr/bin/python3
"""  a script that reads stdin line by line and computes metrics
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size>
"""
import sys


def display_message(dictionary_source, file_size):
    """
    Method to display
    Args:
        dictionary_source: dict of status codes
        file_size: total of the file
    Returns:
        Nothing to display
    """

    print("File size: {}".format(file_size))
    for key, val in sorted(dictionary_source.items()):
        if val != 0:
            print("{}: {}".format(key, val))


T_file_size = 0
code = 0
counter = 0
dictonary_src = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}

try:
    for line in sys.stdin:
        parsed_line = line.split()  # ✄ trimming
        parsed_line = parsed_line[::-1]  # inverting

        if len(parsed_line) > 2:
            counter += 1

            if counter <= 10:
                T_file_size += int(parsed_line[0])  # file size
                code = parsed_line[1]  # status code

                if (code in dictonary_src.keys()):
                    dictonary_src[code] += 1

            if (counter == 10):
                display_message(dictonary_src, T_file_size)
                counter = 0

finally:
    display_message(dictonary_src, T_file_size)