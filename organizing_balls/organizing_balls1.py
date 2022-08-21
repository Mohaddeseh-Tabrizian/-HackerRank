#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'organizingContainers' function below.
#
# The function is expected to return a STRING.
# The function accepts 2D_INTEGER_ARRAY container as parameter.
#

def space_in_each_container(container):
    space_in_each_container = []

    n = len(container)

    for row_num in range(0, n):
        sum = 0
        for collumn_num in range(0, n):
            sum += container[row_num][collumn_num]
        space_in_each_container.append(sum)

    return space_in_each_container


def totall_balls_each_type(container):
    total_balls_of_each_type = []
    counter = 0
    n = len(container)

    for column in range(0, n):
        s = 0
        counter = 0
        while counter != len(container):
            s += container[counter][column]
            counter += 1
        total_balls_of_each_type.append(s)

    return total_balls_of_each_type


def organizingContainers(container):
    n = len(container)
    s1 = space_in_each_container(container)
    s2 = totall_balls_each_type(container)

    s1 = sorted(s1)
    s2 = sorted(s2)

    for i in range(0, n):
        if s1[i] == s2[i]:
            pass
        else:
            return 'Impossible'
    return 'Possible'


if __name__ == '__main__':
    fptr = sys.stdout

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
