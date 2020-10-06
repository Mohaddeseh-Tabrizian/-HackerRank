import math


def find_w_z(n, x, y):
    for z in range(0, 100001):
        # n = w * x + z * y
        w = (n - x * z) / y
        if w == math.floor(w) and w >= 0:
            z = (n - w * y) / x
            if z == math.floor(z) and z >= 0:
                print(int(z), int(w))
                return
    print(-1)


if __name__ == '__main__':
    nxy = list(map(int, input().rstrip().split()))

    n = nxy[0]
    x = nxy[1]
    y = nxy[2]

    find_w_z(n, x, y)
