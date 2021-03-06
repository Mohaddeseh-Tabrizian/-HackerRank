
def enqueue(line, queue):
    element = line.pop()
    queue.append(element)


def dequeue(queue):
    poped = queue.pop(0)


def print_first_element(queue):
    print(queue[0])


if __name__ == '__main__':
    n = int(input())

    queue = []

    for index in range(0, n):
        line = list(map(int, input().split()))

        if line[0] == 1:
            enqueue(line, queue)
        elif line[0] == 2:
            dequeue(queue)
        elif line[0] == 3:
            print_first_element(queue)