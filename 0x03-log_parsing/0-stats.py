#!/usr/bin/python3
"""A script that reads stdin line by line and computes metrics
After every 10 lines and/or a keyboard interruption (CTRL + C), 
print these statistics from the beginning:
"""
import re


def extract_input_HTTP_request(input_line):
    """ Extracts an HTTP request log.
    """
    extr_input = (r'\s*(?P<ip>\S+)\s*', r'\s*\[(?P<date>\d+\-\d+\-\d+ \d+:\d+:\d+\.\d+)\]',r'\s*"(?P<request>[^"]*)"\s*',
        r'\s*(?P<status_code>\S+)', r'\s*(?P<file_size>\d+)' )
    information = {
        'status_code': 0,
        'file_size': 0,
    }
    log_format = '{}\\-{}{}{}{}\\s*'.format(extr_input[0], extr_input[1], extr_input[2], extr_input[3], extr_input[4])
    res_match = re.fullmatch(log_format, input_line)
    if res_match is not None:
        statusCode = res_match.group('statusCode')
        fileSize = int(res_match.group('fileSize'))
        information['statusCode'] = statusCode
        information['fileSize'] = fileSize
    return information
def print_statistics_http(total_size, status_codes):
    """ display the statistics of 
    the HTTP request log.
    """
    print('File size: {:d}'.format(total_size), flush=True)
    for status_code in sorted(status_codes.keys()):
        num = status_codes.get(status_code, 0)
        if num > 0:
            print('{:s}: {:d}'.format(status_code, num), flush=True)
def update_metrics_retrive(line, total_sizes, status_codes):
    """ Metrics from a given HTTP request log.
    Args:
        line (str): The line of input to retrieve the metrics.
    Returns:
        int: The total file size.
    """
    lineInformation = extract_input_HTTP_request(line)
    stat_code = lineInformation.get('status_code', '0')
    if stat_code in status_codes.keys():
        status_codes[stat_code] += 1
    return total_sizes + lineInformation['file_size']
def execute():
    """ Starts the log execuation ."""
    line_numbers = 0
    file_size = 0
    codes_stats = {'200': 0, '301': 0, '400': 0, '401': 0,'403': 0,'404': 0, '405': 0,'500': 0,}
    try:
        while True:
            line = input()
            file_size = update_metrics_retrive(line, file_size, codes_stats,)
            line_num += 1
            if line_num % 10 == 0:
                print_statistics_http(file_size, codes_stats)
    except (KeyboardInterrupt, EOFError):
        print_statistics_http(file_size, codes_stats)


if __name__ == '__main__':
    execute()