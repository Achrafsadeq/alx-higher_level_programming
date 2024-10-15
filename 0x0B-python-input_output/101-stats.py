#!/usr/bin/python3
"""
This script reads lines from standard input, processes log data, and computes
metrics such as total file size and counts of status codes. The metrics are
printed every 10 lines and upon program termination.
"""


def print_stats(size, status_codes):
    """
    Prints the accumulated metrics: total file size and status code counts.

    Args:
        size (int): The total size of all processed requests.
        status_codes (dict): A dictionary where the keys are status codes
        (as strings),and the values are the counts of occurrences
        for each code.
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, status_codes)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in valid_codes:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
