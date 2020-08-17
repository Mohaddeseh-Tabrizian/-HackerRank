#!/bin/python3

import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
sumOfSwaps = 0
for i in range(0, n):
    numSwaps = 0
    for j in range(0, n - 1):
        if a[j] > a[j + 1]:
            a[j + 1], a[j] = a[j], a[j + 1]
            numSwaps += 1
        j += 1
    sumOfSwaps += numSwaps
    if numSwaps == 0:
        break
i += 1

firstElement = a[0]
lastElement = a[n - 1]
print("Array is sorted in " + str(sumOfSwaps) + " swaps.")
print("First element is: " + str(firstElement))
print("Last element is: " + str(lastElement))
