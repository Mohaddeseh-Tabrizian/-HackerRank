#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def quickSort(arr):
    left = []
    right = []
    pivot = arr[0]
    equal = []

    for i in range(len(arr)):
        if arr[i] > pivot:
            right.append(arr[i])
        elif arr[i] < pivot:
            left.append(arr[i])
        elif arr[i] == pivot:
            equal.append(arr[i])

    return left + equal + right


if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
