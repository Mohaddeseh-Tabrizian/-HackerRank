#!/bin/python3

import math
import sys


#
# Complete the 'encryption' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def remove_space(original_string):
    without_spaces_string = ''
    for char in original_string:
        if char == ' ':
            pass
        else:
            without_spaces_string += char
    return without_spaces_string


def determine_floor(L):
    m = math.sqrt(L)
    return math.floor(m)


def determine_ceil(L):
    m = math.sqrt(L)
    return math.ceil(m)


def find_row_collumn(floor, ceil, L):
    second_num = floor * ceil  # second smallest
    first_num = floor * floor  # smallest
    third_num = ceil * ceil  # third smallest

    if first_num >= L:
        return floor, floor
    elif second_num >= L:
        return floor, ceil
    elif third_num >= L:
        return ceil, ceil
    else:
        print('invalid')


def encrypt(without_spaces_string, row, collumn):
    dictionary = {}
    for i in range(1, collumn + 1):
        dictionary[i] = ''

    i = 1
    for element in without_spaces_string:
        if i != collumn + 1:
            dictionary[i] = dictionary[i] + element
            i += 1
        else:
            i = 1
            dictionary[i] = dictionary[i] + element
            i += 1

    return dictionary


def dictionary_to_string(dic, collumn):
    final_string = ''
    for i in range(1, collumn + 1):
        final_string += dic[i]
        if i != collumn:
            final_string += ' '
        else:
            pass
    return final_string


def encryption(s):
    without_spaces_string = remove_space(s)
    L = len(without_spaces_string)

    f = determine_floor(L)
    c = determine_ceil(L)
    row, collumn = find_row_collumn(f, c, L)
    dic = encrypt(without_spaces_string, row, collumn)
    return dictionary_to_string(dic, collumn)


if __name__ == '__main__':
    s = input()

    result = encryption(s)

    print(result)
