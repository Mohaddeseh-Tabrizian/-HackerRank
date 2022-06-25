

import sys
# create a heap with these operations: insert, delete, print_the_minimum.
class MinHeap:
    # creating a somewhat dynamic array.
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.heap = [0] * (self.maxsize + 1)
        self.heap[0] = -1 * sys.maxsize
        self.length_of_arr = 0  # counts the num of elements added
        self.index_of_root = 1 # the first element that we add (one-indexing)

    def parent(self, i):
        return i // 2

    def right_child(self, i):
        return (2 * i) + 1

    def left_child(self, i):
        return 2 * i

    def insert(self, element):
        if self.length_of_arr > self.maxsize:
            return

        self.length_of_arr += 1

        current = self.length_of_arr

        # new node of heap is put in the last element of the array
        self.heap[self.length_of_arr] = element

        # swap if needed to make the heap a min-heap
        while self.heap[current] < self.heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def delete_root(self):
        self.heap[1] = self.heap[self.length_of_arr]
        self.length_of_arr -= 1
        new_root = self.minheapify(1)
        return new_root

    def delete(self, element):
        current = self.heap[1]

        if current is element:
            self.delete_root()
        else:
            index_to_delete = self.search(element)
            self.heap[index_to_delete] = self.heap[self.length_of_arr]
            self.length_of_arr -= 1
            new_root = self.minheapify(index_to_delete)
            return new_root

    def print_minimum(self):
        print(self.heap[1])

    def search(self, element):
        for i in range(1, self.length_of_arr + 1):
            if self.heap[i] == element:
                return i

    # this function is used when u delete root and want to make sure that u still have a minheap
    # recursive implementation with array representation of a tree.
    def minheapify(self, index):
        # but its index should not belong to a leaf node because there are no left and right child for it.
        # then that would return None and then error
        if not self.is_leaf_node(index):
            if (self.heap[index] > self.heap[self.right_child(index)] or self.heap[index] > self.heap[self.left_child(index)]):
                if self.heap[self.left_child(index)] < self.heap[self.right_child(index)]:
                    self.swap(self.left_child(index), index)
                    self.minheapify(self.left_child(index))
                else:
                    self.swap(self.right_child(index), index)
                    self.minheapify(self.right_child(index))
            else:
                return self.heap[1]
        return self.heap[1]

    def is_leaf_node(self, i):
        return i * 2 > self.length_of_arr


def find_operation(func, min_heap):
    if func[0] == 1:
        min_heap.insert(func[1])
    elif func[0] == 2:
        min_heap.delete(func[1])
    else:
        min_heap.print_minimum()


if __name__ == '__main__':
    n = int(input())
    min_heap = MinHeap(n)

    for i in range(n):
        func = list(map(int, input().rstrip().split()))
        find_operation(func, min_heap)

