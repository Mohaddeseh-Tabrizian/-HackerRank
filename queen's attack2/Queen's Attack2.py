#!/bin/python3

import sys


def possibleAttacks(dimension, x, y):
    q = 2 * dimension - 2
    p = 2 * dimension - 2 - abs(x - y) - abs(x + y - dimension - 1)

    return p + q


def getBlockedCells(qx, qy, obstacle_array):
    blocked_cells = set()

    for row in obstacle_array:
        obstacle_x = row[0]
        obstacle_y = row[1]

        relative_direction = findDirection(obstacle_x, obstacle_y, qx, qy)

        if relative_direction == 'north':
            while 1 <= obstacle_x <= n:
                blocked_cells.add((obstacle_x, obstacle_y))
                obstacle_x += 1
        elif relative_direction == 'south':
            while 1 <= obstacle_x <= n:
                blocked_cells.add((obstacle_x, obstacle_y))
                obstacle_x -= 1
        elif relative_direction == 'east':
            while 1 <= obstacle_y <= n:
                blocked_cells.add((obstacle_x, obstacle_y))
                obstacle_y += 1
        elif relative_direction == 'west':
            while 1 <= obstacle_y <= n:
                blocked_cells.add((obstacle_x, obstacle_y))
                obstacle_y -= 1
        elif relative_direction == 'north_east':
            while 1 <= obstacle_x <= n and 1 <= obstacle_y <= n:
                blocked_cells.add((obstacle_x, obstacle_y))
                obstacle_x += 1
                obstacle_y += 1
        elif relative_direction == 'north_west':
            while 1 <= obstacle_x <= n and 1 <= obstacle_y <= n:
                blocked_cells.add((obstacle_x, obstacle_y))
                obstacle_x += 1
                obstacle_y -= 1
        elif relative_direction == 'south_east':
            while 1 <= obstacle_x <= n and 1 <= obstacle_y <= n:
                blocked_cells.add((obstacle_x, obstacle_y))
                obstacle_x -= 1
                obstacle_y += 1
        elif relative_direction == 'south_west':
            while 1 <= obstacle_x <= n and 1 <= obstacle_y <= n:
                blocked_cells.add((obstacle_x, obstacle_y))
                obstacle_x -= 1
                obstacle_y -= 1

    return len(blocked_cells)


def findDirection(obstacle_x, obstacle_y, queen_x, queen_y):
    direction = None

    if obstacle_y == queen_y:
        direction = 'north' if obstacle_x > queen_x else 'south'
    elif obstacle_x == queen_x:
        direction = 'east' if obstacle_y > queen_y else 'west'
    elif isInTheDirectionOfQueen(obstacle_x, obstacle_y, queen_x, queen_y):
        if obstacle_x > queen_x:
            direction = 'north_east' if obstacle_y > queen_y else 'north_west'
        else:
            direction = 'south_east' if obstacle_y > queen_y else 'south_west'

    return direction


def isInTheDirectionOfQueen(r, c, x, y):
    return abs(r - x) == abs(c - y)


def queensAttack(size_of_chess_board, queen_row, queen_column, obstacles_arr):
    num_attacks = possibleAttacks(size_of_chess_board, queen_row, queen_column)

    num_blocked = getBlockedCells(queen_row, queen_column, obstacles_arr)

    return num_attacks - num_blocked


if __name__ == '__main__':
    fptr = sys.stdout

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, r_q, c_q, obstacles)

    print(result)
