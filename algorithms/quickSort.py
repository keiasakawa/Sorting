"""
An implementation of quick sort.

Quick sort works by selecting a pivot given the end ranges of a list.
Using this pivot, two pointers are used: a left one to check if the element is greater than the pivot and 
a right one to check if the element is less than the pivot. Once both these conditions are met, the positions are swapped.
This is repeated until the position of the left pointer is greater than the right pointer. The position of the right pointer
element is then swapped with the pivot element, which is sorted. The algorithm then recursively calls on the both the
right and left side of the pivot.

TIME COMPLEXITY: O(N^2)
SPACE COMPLEXITY: O(1)
"""

def partition(a, l, r):
    pivot = a[l]
    pivotPos = l
    while l < r:
        while l < len(a) and a[l] <= pivot:
            l += 1
        while r > 0 and a[r] > pivot:
            r -= 1
        if l < r:
            a[l], a[r] = a[r], a[l]
    a[r], a[pivotPos] = pivot, a[r]
    return r

def quickSort(a, l, r):
    if l < r:
        pos = partition(a, l, r)
        quickSort(a, l, pos - 1)
        quickSort(a, pos + 1, r)
