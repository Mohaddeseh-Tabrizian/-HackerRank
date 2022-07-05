#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#

def formingMagicSquare(s):
    a = [[6, 1, 8], [7, 5, 3], [2, 9, 4]]
    b = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
    c = [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    d = [[8, 3, 4], [1, 5, 9], [6, 7, 2]]
    e = [[8, 1, 6], [3, 5, 7], [4, 9, 2]]
    f = [[4, 3, 8], [9, 5, 1], [2, 7, 6]]
    g = [[2, 9, 4], [7, 5, 3], [6, 1, 8]]
    h = [[6, 7, 2], [1, 5, 9], [8, 3, 4]]

    matrices = [a, b, c, d, e, f, g, h]

    optimal_cost = 99

    for every_matric in matrices:
        cost = 0
        for i in range(3):
            for j in range(3):
                if s[i][j] != every_matric[i][j]:
                    cost += abs(s[i][j] - every_matric[i][j])

        if cost < optimal_cost:
            optimal_cost = cost

    return optimal_cost


if __name__ == '__main__':
    fptr = sys.stdout

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
