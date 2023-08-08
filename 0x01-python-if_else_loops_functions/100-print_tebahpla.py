#!/usr/bin/python3
for i in range(90, 64, -1):
    print('{}'.format(chr(i + 32)), end='') if i % 2 == 0 else print('{}'.format(chr(i)), end='')
