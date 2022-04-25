#!/bin/python3

import math
import os
import random
import re
import sys
import bisect

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#


def ranks(ranked):
    rank = []

    for i in range(len(ranked)):
        if i == 0:
            rank.append(1)
        elif ranked[i] == ranked[i - 1]:
            rank.append(rank[i - 1])
        elif ranked[i] < ranked[i - 1]:
            rank.append(int(rank[i - 1]) + 1)

    return rank

# with Binary Search, I found the place that the new element should be inserted in.
def find_position_of_rank(ranked, element):
    start = 0
    end = len(ranked) - 1

    while start <= end:
        mid = (end + start) // 2

        if ranked[mid] > element:
            start = mid + 1
        elif ranked[mid] < element:
            end = mid - 1
        elif ranked[mid] == element:
            return mid

    return end + 1


def climbingLeaderboard(ranked, player):
    rank = ranks(ranked)
    new_ranks = []

    for i, element in enumerate(player):
        index = find_position_of_rank(ranked, element)
        if index == 0:
            new_ranks.append(1)
        elif ranked[index - 1] == element:
            new_ranks.append(rank[index - 1])
        elif ranked[index - 1] > element:
            new_ranks.append(int(rank[index - 1]) + 1)

    return new_ranks


if __name__ == '__main__':
    fptr = sys.stdout

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
