#!/bin/python3

import math
import os
import random
import re
import sys


def number_of_layers(m, n):
    if m < n:
        numberoflayers = m // 2
    else:
        numberoflayers = n // 2
    return numberoflayers


def get_column(matrix, column_index):
    column = []

    for row_index in range(0, len(matrix)):
        column.append(matrix[row_index][column_index])

    return column


def get_row_numbers(matrix):
    return len(matrix)


def get_layer(matrix, layer_index):
    layer = []
    column_num = len(matrix[0]) - 1
    row_index = get_row_numbers(matrix) - 1
    right_column_index = column_num - layer_index

    top_row = matrix[layer_index].copy()
    top_row.pop()
    layer.extend(top_row) # top row added
    right_column = get_column(matrix, right_column_index)
    right_column.pop()
    layer.extend(right_column) # right column added
    arr_for_lowest_row = matrix[row_index - layer_index].copy()
    arr_for_lowest_row.reverse()
    arr_for_lowest_row.pop()
    layer.extend(arr_for_lowest_row) # Bottom row added
    arr_for_first_column = get_column(matrix, layer_index)
    arr_for_first_column.reverse()
    arr_for_first_column.pop()
    layer.extend(arr_for_first_column) # Left row column added

    return layer


def get_layers(matrix):
    layers = []

    rows = len(matrix)
    columns = len(matrix[0])

    print(get_layer(matrix, 0))
    exit()
    for layer_index in range(0, number_of_layers(rows, columns)):
        layers.append(get_layer(matrix, layer_index))

    return layers


# def pop_from_every_layer(matrix, layer_index):
#     layer = get_layer(matrix, layer_index)
#     layer_poped = []
#     for list in get_layer(matrix, layer_index):
#         pop_count = pow(2, layer_index)
#         pop_counter = pop_count // 2
#
#         if pop_counter == float:
#             layer_poped.append(layer)
#
#         for i in range(0, pop_counter):
#             list.pop(i)
#             list.pop()
#         list.pop()
#         layer_poped.append(list)
#
#     return layer_poped


# def get_rings(matrix):
#     rings = []
#     for layer_index in range(0, number_of_layers(m, n)):
#         layer_poped = pop_from_every_layer(matrix, layer_index)
#         rings.append(layer_poped)
#     return rings


# def once_layer_rotated(layers):
#     rotated = []
#     for i in range(0, len(layers)):
#         i = i + 1
#         rotated.append(layers[i])
#     return rotated
#
# # Complete the matrixRotation function below.
# def matrixRotation(matrix, r):
#     each_layer_rotated(layers)
#     r_times_rotated = []
#     for i in range(0, r):
#
#         layers[i][j]


if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    print(get_layers(matrix))

    # matrixRotation(matrix, r)

