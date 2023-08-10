#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    num_args = len(argv) - 1
    result = 0

    if num_args > 0:
        for i in range(1, num_args + 1):
            result += int(argv[i])

    print(result)
