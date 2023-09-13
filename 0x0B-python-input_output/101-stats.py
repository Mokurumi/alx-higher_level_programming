#!/usr/bin/python3
'''
module to read in line by line and compute metrics
'''


import sys


def print_metrics(size, stat_codes):
    """
    Prints the total file size and counts of each HTTP status code.

    Args:
        size (int): Total file size.
        stat_codes (dict):
            Dictionary containing counts of each HTTP status code.
    """
    print("File size: {:d}".format(size))
    for k, v in sorted(stat_codes.items()):
        if v:
            print("{:s}: {:d}".format(k, v))


def compute_metrics():
    """
    Parses input lines from the standard input and computes metrics.

    This function reads lines from the standard input, extracts the file size
        and HTTP status code from each line, and computes the total file size
        and counts of each HTTP status code.
        It prints the metrics every 10 lines.

    Returns:
        None
    """
    size = 0
    lines = 0
    stat_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                  "403": 0, "404": 0, "405": 0, "500": 0}
    try:
        for line in sys.stdin:
            fields = list(map(str, line.strip().split(" ")))
            size += int(fields[-1])
            if fields[-2] in stat_codes:
                stat_codes[fields[-2]] += 1
            lines += 1
            if lines % 10 == 0:
                print_metrics(size, stat_codes)
    except KeyboardInterrupt:
        print_metrics(size, stat_codes)
        raise

    print_metrics(size, stat_codes)

# Execute the parsing and computing function
compute_metrics()
