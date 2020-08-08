

def binary(num):
    machin_code = []

    p = 1
    while num > 1:
        p = num // 2
        q = num % 2
        machin_code.append(q)
        num = p
    machin_code.append(p)
    machin_code.reverse()

    return machin_code


def find_maximum_consecutive_ones(machine_code):
    count_of_ones = []
    counter = 0
    last_index = len(machine_code) - 1

    for index, x in enumerate(machine_code):
        if x == 1:
            counter += 1
        else:
            count_of_ones.append(counter)
            counter = 0
        if index == last_index:
            count_of_ones.append(counter)

    if len(count_of_ones) > 1:
        max_count_of_ones = max(count_of_ones)
    else:
        max_count_of_ones = count_of_ones[0]

    return max_count_of_ones


if __name__ == '__main__':
    num = int(input())

    print(find_maximum_consecutive_ones(binary(num)))

