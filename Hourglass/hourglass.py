# !/bin/python3


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    max_sum = []
    for i in range(4):
        for j in range(4):
            sum_of_hourglass = 0
            hour_glass = [arr[i][j], arr[i][j + 1], arr[i][j + 2], arr[i + 1][j + 1],
                          arr[i + 2][j], arr[i + 2][j + 1], arr[i + 2][j + 2]]
            for x in hour_glass:
                sum_of_hourglass += x
            max_sum.append(sum_of_hourglass)
    answer = max(max_sum)
    print(answer)

