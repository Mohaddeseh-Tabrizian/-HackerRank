#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below. (determinant)
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):
    s_diagnal = 0
    s_anti_diagnal = 0

    n = len(arr)

    for row in range(0, n):
        s_diagnal += arr[row][row]

    column_counter = 0
    for row in range(n, 0, -1):
        s_anti_diagnal += arr[row - 1][column_counter]
        column_counter += 1

    return abs(s_diagnal - s_anti_diagnal)


if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
