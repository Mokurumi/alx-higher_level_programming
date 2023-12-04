#!/usr/bin/python3
'''
Find a peak in a list of unsorted integers using a divide-and-conquer strategy
'''

def find_peak(list_of_integers):
    """
    Args:
    - list_of_integers: A list of unsorted integers.

    Returns:
    - The peak element from the list.
    - None if the list is empty.
    """
    # Check if the list is empty
    if not list_of_integers:
        return None

    # Define the low and high indices
    low = 0
    high = len(list_of_integers) - 1

    # Perform binary search to find the peak
    while low < high:
        # Calculate the mid index
        mid = (low + high) // 2

        # Compare the element at the mid index with the next element
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            # If current element < next element, move low to mid + 1
            low = mid + 1
        else:
            # If current element is greater, move high to mid
            high = mid

    # Return the element at the low index, which represents a peak
    return list_of_integers[low]
