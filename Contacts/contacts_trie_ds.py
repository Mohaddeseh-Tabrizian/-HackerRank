#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'contacts' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY queries as parameter.
#
# function is a string that represents the kind of function(add, find)


class TrieNode:
    def __init__(self, is_end_of_word=False):
        self.children = [None] * 29
        self.is_end_of_word = is_end_of_word
        self.num_of_descendant = 0

    def increment_num_of_descendant(self):
        self.num_of_descendant += 1


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def char_to_index(self, ch):
        return ord(ch) - ord('a')

    def add(self, word):
        current = self.root
        length = len(word)

        for i in range(length + 1):
            current.increment_num_of_descendant()

            if i == length:
                current.is_end_of_word = TrieNode(True)
                break

            index = self.char_to_index(word[i])

            if not current.children[index]:
                current.children[index] = TrieNode()

            current = current.children[index]  # from root to this node

    def find(self, word):
        num_of_words_with_same_prefix = 0
        current = self.root
        length = len(word)

        for i in range(length):
            index = self.char_to_index(word[i])

            if not current.children[index]:
                return num_of_words_with_same_prefix

            current = current.children[index]

        num_of_words_with_same_prefix = current.num_of_descendant

        return num_of_words_with_same_prefix


def find_function(element):
    function = element[0]
    word = element[1]
    return function, word


def contacts(queries):  # int[]
    result = []
    t = Trie()
    for element in queries:
        function, word = find_function(element)
        if function == 'add':
            t.add(word)
        elif function == 'find':
            result.append(t.find(word))

    return result


if __name__ == '__main__':
    fptr = sys.stdout

    queries_rows = int(input().strip())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
