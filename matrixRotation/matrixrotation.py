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


def get_column(matrix, column_index, layer_index):
    column = []

    end_index = len(matrix) - layer_index
    for row_index in range(layer_index, end_index):
        column.append(matrix[row_index][column_index])

    return column


def get_row(matrix, row_index, layer_index):
    row = matrix[row_index]
    end_index = len(matrix[0]) - layer_index

    return row[layer_index:end_index]


def get_row_numbers(matrix):
    return len(matrix)


def get_layer(matrix, layer_index):
    layer = []
    column_num = len(matrix[0]) - 1
    row_index = get_row_numbers(matrix) - 1
    right_column_index = column_num - layer_index

    top_row = get_row(matrix, layer_index, layer_index)
    top_row.pop()
    layer.extend(top_row)  # top row added
    right_column = get_column(matrix, right_column_index, layer_index)
    right_column.pop()
    layer.extend(right_column)  # right column added
    arr_for_lowest_row = get_row(matrix, row_index - layer_index, layer_index)
    arr_for_lowest_row.reverse()
    arr_for_lowest_row.pop()
    layer.extend(arr_for_lowest_row)  # Bottom row added
    arr_for_first_column = get_column(matrix, layer_index, layer_index)
    arr_for_first_column.reverse()
    arr_for_first_column.pop()
    layer.extend(arr_for_first_column)  # Left row column added

    return layer


def get_layers(matrix):
    layers = []

    rows = len(matrix)
    columns = len(matrix[0])

    for layer_index in range(0, number_of_layers(rows, columns)):
        layers.append(get_layer(matrix, layer_index))

    return layers


def rotate_each_layer_r_times(layer, rotation_count):
    rotation_count = rotation_count % len(layer)
    i = 0
    while i < rotation_count:
        poped = layer.pop(0)
        layer.append(poped)
        i += 1
    return layer


def create_empty_matrix(rows, columns):
    matrix = []
    for i in range(0, rows):
        row = []
        for column in range(0, columns):
            row.append(0)
        matrix.append(row)
    return matrix


def fill_row(row_index, column_index, matrix, data):
    for i in range(0, len(data)):
        matrix[row_index][i + column_index] = data[i]

    return matrix


def fill_column(column_index, row_index, matrix, data):
    for j in range(0, len(data)):
        matrix[j + row_index][column_index] = data[j]

    return matrix


def fill_matrix(matrix, layers):
    row_count = get_row_numbers(matrix)
    column_count = len(matrix[0])
    new_matrix = create_empty_matrix(row_count, column_count)
    layer_row_count = row_count
    layer_column_count = column_count
    for layer_index, layer in enumerate(layers):
        layer_row_count = row_count - (layer_index * 2)
        layer_column_count = column_count - (layer_index * 2)

        new_matrix = fill_row(layer_index, layer_index, new_matrix, layer[0:layer_column_count])

        end_index_for_slice = layer_column_count + layer_row_count - 1
        new_matrix = fill_column(column_count - layer_index - 1, layer_index + 1, new_matrix,
                                 layer[layer_column_count:end_index_for_slice])

        new_end_index_for_slice = end_index_for_slice + layer_column_count - 1
        data = layer[end_index_for_slice:new_end_index_for_slice]
        data.reverse()
        new_matrix = fill_row(row_count - layer_index - 1, layer_index, new_matrix, data)

        data = layer[new_end_index_for_slice:]
        data.reverse()
        new_matrix = fill_column(layer_index, layer_index + 1, new_matrix, data)

    return new_matrix


def print_matrix(matrix):
    column_count = len(matrix[0])
    last_column_index = column_count - 1
    for i in range(0, len(matrix)):
        for j in range(0, column_count):
            if j == last_column_index:
                print(matrix[i][j])
            else:
                print(matrix[i][j], end=' ')


# Complete the matrixRotation function below.
def matrixRotation(matrix, r):
    layers = get_layers(matrix)
    for layer in layers:
        rotate_each_layer_r_times(layer, r)
    empty_matrix = create_empty_matrix(get_row_numbers(matrix), len(matrix[0]))
    matrix_rotated = fill_matrix(empty_matrix, layers)
    print_matrix(matrix_rotated)


if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
