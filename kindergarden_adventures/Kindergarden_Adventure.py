#!/bin/python3

import os
import sys
# The first line contains a single positive integer, n, denoting the number of students in the class.
# The second line contains n space-separated integers describing the respective amounts of time that each student needs to finish their drawings

#Print an integer denoting the ID number, x, where Meera should start collecting the drawings such that a maximal number of students can complete their drawings. If there are multiple such IDs, select the smallest one.

    
def create_dictionary(n):
    finished_students = {}
    variable = 0
    for i in range(n):
        finished_students[i] = variable
    return finished_students


def fill_dic_with_ranges(finished_students, f, s, n):
    for seat in range(n):
        if seat in f:
            finished_students[seat] += 1
        elif seat in s:
            finished_students[seat] += 1
        else:
            finished_students[seat] -= 1

    return finished_students


def fill_dic_with_start_and_end(finished_students, f, s, n):
    this_range = range(f, s + 1)
    for seat in range(n):
        if seat in this_range:
            finished_students[seat] += 1
        else:
            finished_students[seat] -= 1

    return finished_students


def find_the_happiness_range(value, i, n, t):
    t = t + t
    # concatenated[i: i + (n-1)]
    start = i+1
    end = (i + n - 1) - (value - 1)
    f, s = equalizing(start, end, n)
    return f, s


def equalizing(start, end, n):

    if (0 < start < (n - 1)) and (0 < end < (n - 1)):
        return start, end

    if end >= n:
        second_block = end - (n - 1)
        second_range = range(0, second_block)
    else:
        second_range = range(start, (n - 1))

    if start == n:
        first_range = second_range
    else:
        first_range = range(start, (n - 1))

    return first_range, second_range


def solve(t):
    n = len(t)
    finished_students = create_dictionary(n)
    for i in range(n):
        if t[i] == 0 or t[i] == n:
            continue

        f, s = find_the_happiness_range(t[i], i, n, t)

        if isinstance(f, int):
            finished_students = fill_dic_with_start_and_end(finished_students, f, s, n)
        else:
            finished_students = fill_dic_with_ranges(finished_students, f, s, n)

    chosen_value = float('-inf')
    starting_index = 0
    for i in range(n):
        if finished_students[i] > chosen_value:
            chosen_value = finished_students[i]
            starting_index = i
    return starting_index + 1


if __name__ == '__main__':
    fptr = sys.stdout

    t_count = int(input())

    t = list(map(int, input().rstrip().split()))

    id = solve(t)

    fptr.write(str(id) + '\n')

    fptr.close()
