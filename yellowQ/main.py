

def print_surprize_size(n):
    print('W', end='')
    for i in range(0, n):
        print('o', end='')
    print('w!', end='')


if __name__ == '__main__':
    n = int(input())
    print_surprize_size(n)
