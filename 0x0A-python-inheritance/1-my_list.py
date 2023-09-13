#!/usr/bin/python3
'''module to print a sorted list'''


class MyList(list):
    """
    a class that inherits from list
    """

    def append(self, item):
        """
        Override the append method to add an item to the list.

        Args:
        item: The item to be added to the list.
        """
        super().append(item)  # Call the parent class's append method

    def print_sorted(self):
        """
        Sorts and prints the elements of the list in ascending order.

        Example:
        my_list = MyList([3, 1, 2, 4, 5])
        my_list.print_sorted()  # Output: 1 2 3 4 5
        """
        print(sorted(self))
