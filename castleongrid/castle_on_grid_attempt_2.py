#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'minimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY grid
#  2. INTEGER startX
#  3. INTEGER startY
#  4. INTEGER goalX
#  5. INTEGER goalY
#


def minimumMoves(grid, startX, startY, goalX, goalY):
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]  # the question needs moving in 4 directions not more.
    visit = set()  # set is good cause it drops out repetitious elements.
    moves = 0
    q = deque([[startX, startY, moves]])  # it is just a little faster to deal with poping and appending.
    while q:
        path_x, path_y, moves = q.popleft()
        moves += 1  # until changing the coordinates the move is the same no matter what direction from that cordinate.
        for xi, yi in directions:
            x, y = path_x, path_y
            while True:  # continue in this direction until condition does not satisfy.
                x = x + xi
                y = y + yi
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == '.':
                    if x == goalX and y == goalY:
                        return moves
                    elif (x, y) not in visit:
                        visit.add((x, y))
                        q.append([x, y, moves])
                else:  # change the direction.
                    break
    return -1  # when q is empty and we didn't find the moves --> it means there are no moves.


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    first_multiple_input = input().rstrip().split()

    startX = int(first_multiple_input[0])

    startY = int(first_multiple_input[1])

    goalX = int(first_multiple_input[2])

    goalY = int(first_multiple_input[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + '\n')

    fptr.close()
