#  if u limit urself to just some data structures yyou will find it hard to solve
# problems in programming but if u look at the logic open minded and consider all the correct
#  data structures and use ur creativvity probably u will find the best logic for the problem
# !/bin/python3

import math
import os
import random
import re
import sys
from math import sqrt
from collections import deque

def downToZero(n):
    memory = set()
    count = 0
    que = deque([[n, count]])
    while que:
        n, count = que.popleft()
        if n <= 1:
            if n == 1:
                count += 1
            break

        # second operation
        if n-1 not in memory:
            memory.add(n-1)
            que.append([n-1, count+1])

        # first operation
        for i in range(int(sqrt(n)), 1, -1):
            if n % i == 0:
                factor = max(n//i, i)
                if factor not in memory:
                    memory.add(factor)
                    que.append([factor, count + 1])
    return count


if __name__ == '__main__':
    fptr = sys.stdout

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = downToZero(n)

        fptr.write(str(result) + '\n')

    fptr.close()