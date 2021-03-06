#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#



def equalStacks(h1, h2, h3):
    # Write your code here
    firstStack = sum(h1)
    secondStack = sum(h2)
    thirdStack = sum(h3)


    while True:
        if firstStack == 0 or secondStack == 0 or thirdStack == 0:
            return 0
        elif firstStack == secondStack and secondStack == thirdStack and firstStack == thirdStack:
            return firstStack
        else:
            if firstStack > secondStack and firstStack > thirdStack:
                poped = h1.pop(0)
                firstStack = firstStack - poped
            elif secondStack > firstStack and secondStack > thirdStack:
                poped = h2.pop(0)
                secondStack = secondStack - poped
            elif thirdStack > secondStack and thirdStack > firstStack:
                poped = h3.pop(0)
                thirdStack = thirdStack - poped
            elif firstStack == secondStack and firstStack > thirdStack:
                poped = h1.pop(0)
                firstStack = firstStack - poped
            elif secondStack == thirdStack and secondStack > firstStack:
                poped = h2.pop(0)
                secondStack = secondStack - poped
            elif firstStack == thirdStack and firstStack > secondStack:
                poped = h3.pop(0)
                thirdStack = thirdStack - poped



if __name__ == '__main__':
    fptr = sys.stdout

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
