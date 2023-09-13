#!/usr/bin/python3
'''module to print a sorted list'''


class MyList(list):
    """
    a class that inherits from list
    """

    def print_sorted(self):
        """
        Sorts and prints the elements of the list in ascending order.

        Example:
        my_list = MyList([3, 1, 2, 4, 5])
        my_list.print_sorted()  # Output: 1 2 3 4 5
        """
        print(sorted(self))
