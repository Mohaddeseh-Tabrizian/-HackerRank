

def print_paskal_triangle(n):
    previous_arr = []

    for i in range(1, n + 1):
        current_arr = []
        s = ' '
        if i == 1:
            current_arr.append(1)
        if i == 2:
            previous_arr.append(1)
            current_arr = previous_arr
        if i > 2:
            current_arr.append(1)
            for i in range(0, len(previous_arr) - 1):
                current_arr.append(previous_arr[i] + previous_arr[i + 1])
            current_arr.append(1)

        print(' '.join(map(str, current_arr)))
        previous_arr = current_arr


if __name__ == '__main__':
    n = int(input())
    print_paskal_triangle(n)
