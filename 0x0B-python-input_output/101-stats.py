#!/usr/bin/python3


import sys


def print_statistics(total_size, status_counts):
    print("File size: {}".format(total_size))
    for status_code, count in sorted(status_counts.items()):
        print("{}: {}".format(status_code, count))


total_size = 0
status_counts = {}

try:
    line_count = 0
    for line in sys.stdin:
        line_count += 1
        parts = line.split(" ")
        if len(parts) >= 7:
            status_code = parts[-2]
            if status_code in ("200", "301", "400", "401", "403", "404", "405", "500"):
                total_size += int(parts[-1])
                if status_code in status_counts:
                    status_counts[status_code] += 1
                else:
                    status_counts[status_code] = 1

        if line_count % 10 == 0:
            print_statistics(total_size, status_counts)

except KeyboardInterrupt:
    print_statistics(total_size, status_counts)
