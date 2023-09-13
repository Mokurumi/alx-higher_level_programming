#!/usr/bin/python3
'''module to print a sorted list'''


class MyList(list):
    def print_sorted(self):
        """
        Prints the elements of the list in ascending order.
        """
        sorted_list = sorted(self)
        for item in sorted_list:
            print(item, end=' ')
        print()  # Print a newline at the end
