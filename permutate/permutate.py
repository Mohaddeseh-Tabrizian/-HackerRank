#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'absolutePermutation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER k
#

def absolutePermutation(n, k):
    permutations = [None] * n

    for i in range(1, n + 1):
        value_before = i - k - 1
        value_after = i + k - 1
        if(value_before >= 0 and value_before < n and permutations[value_before] == None):
            permutations[value_before] = i
        elif(value_after >= 0 and value_after < n and permutations[value_after] == None):
            permutations[value_after] = i
        else:
            return [-1]

    return permutations


if __name__ == '__main__':
    fptr = sys.stdout

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
