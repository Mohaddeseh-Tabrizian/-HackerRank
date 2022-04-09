#!/bin/python3

import math
import os
import random
import re
import sys


def update_area(area, max_area):
    if area > max_area:
        max_area = area
    return max_area


def calculate_are(left_pointer_index, right_pointer_index, length):
    width = right_pointer_index - left_pointer_index + 1
    area = width * length
    return area


def largestRectangle(h):
    max_area = 0
    for i in range(len(h)):
        right_pointer_index = i
        left_pointer_index = i

        # trace to right
        while right_pointer_index != len(h) - 1 and h[right_pointer_index + 1] >= h[i]:
            right_pointer_index += 1
        # trace to left
        while left_pointer_index != 0 and h[left_pointer_index - 1] >= h[i]:
            left_pointer_index -= 1

        area = calculate_are(left_pointer_index, right_pointer_index, h[i])
        max_area = update_area(area, max_area)
    return max_area


if __name__ == '__main__':
    fptr = sys.stdout

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()

