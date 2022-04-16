#!/bin/python3

import math
import os
import random
import re
import sys

sys.setrecursionlimit(10000)


def find_min_index(h, left, right):
    min_index = left
    for i in range(left, right + 1):
        if h[i] < h[min_index]:
            min_index = i

    return min_index


# left and right are indexes. max_area_histogram is the recursive method.


def max_area_histogram(left, right, h, area):
    # condition for stopping recursion
    if left == right:
        return max(area, h[left])

    index = find_min_index(h, left, right)

    area = max(area, h[index] * (right - left + 1))

    if index + 1 <= right:
        area = max_area_histogram(index + 1, right, h, area)

    if index - 1 >= left:
        area = max_area_histogram(left, index - 1, h, area)

    return area


def largestRectangle(h):
    return max_area_histogram(0, len(h) - 1, h, 0)


if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
