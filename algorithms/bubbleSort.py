"""
An implementation of bubble sort. 

Bubble sort works by comparing an element to the right element and 
if the element is greater, both elements are swapped. This is done at every position
until the last element is swapped. In this case, the greatest element is sorted at each iteration.

TIME COMPLEXITY: O(N^2)
SPACE COMPLEXITY: O(1)

"""

def bubbleSort(l):
    for i in range(len(l) - 1):
        for j in range(len(l) - i - 1):
            if l[j] > l[j + 1]:
                l[j + 1], l[j] = l[j], l[j + 1]


