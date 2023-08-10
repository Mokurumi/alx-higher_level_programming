#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import *


if __name__ == "__main__":
    if len(argv) != 4:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    operator = argv[2]
    result = 0
    a, b = int(argv[1]), int(argv[3])

    if operator  == "+":
        result = add(a, b)
    elif operator  == "-":
        result = sub(a, b)
    elif operator  == "*":
        result = mul(a, b)
    elif operator  == "/":
        result = div(a, b)
    else:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

    print('{} {} {} = {}'.format(a, operator, b, result))
