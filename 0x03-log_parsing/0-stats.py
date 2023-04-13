#!/usr/bin/python3
"""  a script that reads stdin line by line and computes metrics
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
"""
import sys


def print_message(dictonary_source, file_size):
    """
    Method to display the message
    Args:
        dictonary_source: dict of status codes
        file_size: total of the file
    Returns:
        Nothing returns to caller func
    """

    print("File size: {}".format(file_size))
    for key, value in sorted(dictonary_source.items()):
        if value != 0:
            print("{}: {}".format(key, value))


file_size = 0
file_code = 0
count = 0
dictonary_source = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
for lines in sys.stdin:
        pars_line = lines.split() 
        pars_line = pars_line[::-1]  

        if len(pars_line) > 2:
            count += 1

            if count <= 10:
                file_size += int(pars_line[0])  
                file_code = pars_line[1]  

                if (file_code in dictonary_source.keys()):
                    dictonary_source[file_code] += 1

            if (count == 10):
                print_message(dictonary_source, file_size)
                counter = 0

print_message(dictonary_source, file_size)