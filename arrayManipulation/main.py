#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    #creating a 1 indexed array with n nodes
    arr = [0] * (n+2)

    for a,b,k in queries:
        arr[a] += k
        arr[b + 1] -= k
    print(arr)
    maximum = temp = 0
    for val in arr:
        temp += val
        maximum = max(maximum,temp)
    return maximum


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
