#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list.sort()
    sum = 0
    for i in range(0, len(my_list)):
        if i == 0 or my_list[i] != my_list[i - 1]:
            sum += my_list[i]

    return sum
