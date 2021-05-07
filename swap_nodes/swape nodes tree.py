from collections import deque

class Node:
    def __init__(self, index):
        self.left = None
        self.index = index
        self.right = None

def inorder_traversal(root):
    stack = deque([root])
    visited = set()
    while stack:
        node = stack.pop()
        if node is None:
            continue
        if node.index in visited:
            print(node.index, end=' ')
            continue
        visited.add(node.index)  # its a set then its not gonna add node to here if it is already in visited
        stack.append(node.right)
        stack.append(node)
        stack.append(node.left)


def swapNodes(root, k):
    d = deque([(root, 1)])
    while d:
        node, level = d.popleft()
        if node is None:
            continue
        if level % k == 0:
            node.left, node.right = node.right, node.left
        d.append((node.left, level + 1))
        d.append((node.right, level + 1))


if __name__ == '__main__':
    n = int(input())

    nodes = [None]*(n+1)
    # create nodes list
    for i in range(1, n+1):
        n = Node(i)
        n.left_index, n.right_index = [v if v > 0 else 0 for v in map(int, input().split())]
        nodes[i] = n

    # complete node objects
    for n in nodes[1:]:
        left = nodes[n.left_index]
        right = nodes[n.right_index]
        n.left = left
        n.right = right

    queries_count = int(input())

    root = nodes[1]

    for _ in range(queries_count):
        queries_item = int(input())
        result = swapNodes(root, queries_item)
        inorder_traversal(root)
        print('')
