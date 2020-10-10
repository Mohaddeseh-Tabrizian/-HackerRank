def find_rotation(digit, numbers):
    rotation_count = numbers.index(digit)

    if rotation_count > 4:
        rotation_count = 9 - rotation_count

    return rotation_count


if __name__ == '__main__':
    n = int(input())
    secret = list(input())

    rotation_count = 0
    for index in range(0, n):
        numbers = input().rstrip()
        digit = secret[index]

        rotation_count += find_rotation(digit, numbers)

    print(rotation_count)