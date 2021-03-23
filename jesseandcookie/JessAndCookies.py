#!/bin/python3

import os
import sys
import heapq

#
# Complete the cookies function below.
#


def cookies(k, A):
    heapq.heapify(A)

    result = 0
    while True:
        if len(A) == 1:
            if A[0] < k:
                return -1

        first_min = heapq.heappop(A)

        if first_min >= k:
            return result

        if A:
            second_min = heapq.heappop(A)

            sweatness = first_min + (second_min * 2)

            heapq.heappush(A, sweatness)

            result = result + 1
        else:
            return -1



if __name__ == '__main__':
    fptr = sys.stdout

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
