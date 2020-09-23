#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#
class DynamicArray:
    def __init__(self, n):
        self.n = n
        self.lastAnswer = 0
        self.seqList = []
        self.set_sequence_list()

    def set_sequence_list(self):
        for i in range(0, self.n):
            self.seqList.append([])

    def find_sequence(self, x):
        index = (x ^ self.lastAnswer) % n

        return self.seqList[index]

    def query_type_one(self, x, y):
        sequence = self.find_sequence(x)
        sequence.append(y)

    def query_type_two(self, x, y):
        sequence = self.find_sequence(x)
        size = len(sequence)
        index = y % size
        value = sequence[index]
        self.lastAnswer = value

        return self.lastAnswer


def dynamicArray(n, queries):
    # Write your code here
    array = DynamicArray(n)
    dynamicarray_result = []

    for query in queries:
        if query[0] == 1:
            array.query_type_one(query[1], query[2])
        else:
            result_for_type_two = array.query_type_two(query[1], query[2])
            dynamicarray_result.append(result_for_type_two)

    return dynamicarray_result


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = sys.stdout

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
