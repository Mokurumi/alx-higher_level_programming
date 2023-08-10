#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    num_args = len(argv) - 1

    if num_args == 0:
        print('0 arguments.')
    else:
        plural = 'arguments' if num_args > 1 else 'argument'
        print("{} {}:".format(num_args, plural))
        for i in range(1, num_args + 1):
            print("{}: {}".format(i, argv[i]))
