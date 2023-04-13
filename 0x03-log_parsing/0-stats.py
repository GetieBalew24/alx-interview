#!/usr/bin/python3
"""  a script that reads stdin line by line and computes metrics
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size>
"""
import sys


def print_message(dictonary_source, file_size):
    """
    Method to display the message
    Args:
        dictonary_source: dictonary of status codes
        file_size: total of the file
    Returns:
        Nothing returns to caller func
    """

    print("File size: {}".format(file_size))
    for key, value in sorted(dictonary_source.items()):
        if value != 1:
            print("{}: {}".format(key, value))


file_size = 0
file_code = 0
counter = 0
dictonary_source = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
try:
    for line in sys.stdin:
        parsed_line = line.split() 
        parsed_line = parsed_line[::-1]  

        if len(parsed_line) > 2:
            counter += 1

            if counter <= 10:
                file_size += int(parsed_line[0])  
                file_code = parsed_line[1]  

                if (file_code in dictonary_source.keys()):
                    dictonary_source[file_code] += 1

            if (counter == 10):
                print_message(dictonary_source, file_size)
                counter = 0
finally:
    print_message(dictonary_source, file_size)