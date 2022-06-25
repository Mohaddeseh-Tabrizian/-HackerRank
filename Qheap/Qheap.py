

import heapq
# Implementting operations in a heap
if __name__ == '__main__':
    n = int(input())
    heap = []
    d = {}

    for i in range(n):
        func = list(map(int, input().rstrip().split()))

        if func[0] == 1:
            heapq.heappush(heap, func[1])
        elif func[0] == 2:
            if func[1] in d:
                d[func[1]] += 1
            else:
                d[func[1]] = 1
        else:
            while True:
                x = heap[0]
                if x in d:
                    heapq.heappop(heap)
                    d[x] -= 1
                    if d[x] <= 0:
                        del(d[x])
                else:
                    break
            print(x)