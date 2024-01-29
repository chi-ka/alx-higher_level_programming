#!/usr/bin/python3
"""
This module contains a function to find a peak element in a list of unsorted integers.
"""

def find_peak(list_of_integers):
    """
    Find a peak element in a list of unsorted integers.

    A peak element is an element that is greater than or equal to its neighbors.

    Args:
        list_of_integers: A list of integers.

    Returns:
        An integer which is a peak element in the list, or None if the list is empty.
    """
    if not list_of_integers:
        return None

    def _find_peak(arr, low, high, n):
        """
        Helper function to find a peak element using a modified binary search algorithm.

        Args:
            arr: The list of integers.
            low: The starting index of the list to be searched.
            high: The ending index of the list to be searched.
            n: Length of the list.

        Returns:
            An integer which is a peak element in the specified range of the list.
        """
        mid = low + (high - low) // 2

        if ((mid == 0 or arr[mid - 1] <= arr[mid]) and 
            (mid == n - 1 or arr[mid + 1] <= arr[mid])):
            return arr[mid]

        elif mid > 0 and arr[mid - 1] > arr[mid]:
            return _find_peak(arr, low, mid - 1, n)

        else:
            return _find_peak(arr, mid + 1, high, n)

    n = len(list_of_integers)
    return _find_peak(list_of_integers, 0, n - 1, n)

