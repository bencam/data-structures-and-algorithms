#!/usr/bin/env python


def binary_search(input_array, value):
    """Returns the index of the value passed in or a -1 if
    the value does not exist in the list.
    Assumes the array (input_array) contains only unique items
    Assumes the array is organized in increasing order"""
    low = 0
    high = len(input_array) - 1
    while low <= high:
        mid = (low + high) / 2
        if input_array[mid] == value:
            return mid
        elif value > input_array[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1
