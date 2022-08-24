#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#


def find_pivot(w):  # compare string elements two by two
    i = len(w) - 1
    while i > 0 and w[i - 1] >= w[i]:
        i -= 1

    if i <= 0:  # string is empty or has just one element or after loop it did not reach the condition.
        return -1  #  no answer

    return i - 1  # pivot_index


def find_minimum_that_is_bigger(original_string, pivot):
    temp = original_string[pivot+1:]
    t = sorted(temp)
    for i in range(0, len(t)):
        if t[i] > original_string[pivot]:
            return t[i]
        else:
            pass


def swap(original_string, pivot, s):
    temp = list(original_string)  # this syntax is for converting string to array.
    for i in range(pivot+1, len(original_string)):
        if original_string[i] == s:
            temp[i], temp[pivot] = temp[pivot], temp[i]  # this syntax is not for string
            s_final = ''.join(temp)  # this syntax is for converting array to string
            return s_final
        else:
            pass


def sort_after_pivot(original_string, pivot):
    temp = list(original_string)
    temp[pivot + 1:] = sorted(temp[pivot + 1:])
    f = ''.join(temp)
    return f


def biggerIsGreater(original_string):
    pivot = find_pivot(original_string)
    if pivot == -1:
        return 'no answer'
    else:
        s = find_minimum_that_is_bigger(original_string, pivot)
        original_string = swap(original_string, pivot, s)
        r = sort_after_pivot(original_string, pivot)
        return r


if __name__ == '__main__':
    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        print(result)
