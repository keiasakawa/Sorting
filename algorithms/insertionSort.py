"""
A simple implementation of insertion sort. 

Insertion sort works by comparing an element to its predecessor and 
if the element is less than the predecessor, both elements are swapped.
This process is repeated until the element is sorted. The algorithm then moves onto the next element to sort,
which is the element after the original position of the previous element.

TIME COMPLEXITY: O(N^2)
SPACE COMPLEXITY: O(1)

"""

def insertionSort(l):
    for i in range(1, len(l)):
        cur = i
        while cur > 0 and  l[cur] < l[cur - 1]:
            l[cur - 1], l[cur] = l[cur], l[cur - 1]
            cur -= 1
