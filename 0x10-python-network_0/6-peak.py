#!/usr/bin/python3
"""
A function that finds a peak in a list of unsorted integers.
"""

def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    size = len(list_of_integers)
    start = 0
    end = size - 1

    while start < end:
        mid = (start + end) // 2
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            end = mid
        else:
            start = mid + 1

    return list_of_integers[start]
