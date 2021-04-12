#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the isBalanced function below.
def isBalanced(s):
    stacked_brackets = []

    for i in range(len(s)):
        if len(stacked_brackets) == 0:
            top_of_stack = s[i]
            stacked_brackets.append(s[i])
        elif top_of_stack == '{':
            if s[i] == '}':
                stacked_brackets.pop()
                if len(stacked_brackets) > 0:
                    index_now = len(stacked_brackets) - 1
                    top_of_stack = stacked_brackets[index_now]
                else:
                    top_of_stack = ''
            else:
                top_of_stack = s[i]
                stacked_brackets.append(s[i])
        elif top_of_stack == '[':
            if s[i] == ']':
                stacked_brackets.pop()
                if len(stacked_brackets) > 0:
                    index_now = len(stacked_brackets) - 1
                    top_of_stack = stacked_brackets[index_now]
                else:
                    top_of_stack = ''
            else:
                top_of_stack = s[i]
                stacked_brackets.append(s[i])
        elif top_of_stack == '(':
            if s[i] == ')':
                stacked_brackets.pop()
                if len(stacked_brackets) > 0:
                    index_now = len(stacked_brackets) - 1
                    top_of_stack = stacked_brackets[index_now]
                else:
                    top_of_stack = ''
            else:
                top_of_stack = s[i]
                stacked_brackets.append(s[i])
        else:
            top_of_stack = s[i]
            stacked_brackets.append(s[i])

    if len(stacked_brackets) == 0:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    fptr = sys.stdout

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
