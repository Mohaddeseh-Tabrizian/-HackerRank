class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""


def process_tree(root, nodes_not_traversed):

    if root is None:
        return
    else:
        print(root.info, end=' ')

    if len(nodes_not_traversed) > 0:
        nodes_not_traversed.pop(0)

    if root.left:
        nodes_not_traversed.append(root.left)

    if root.right:
        nodes_not_traversed.append(root.right)

    if len(nodes_not_traversed) > 0:
        process_tree(nodes_not_traversed[0], nodes_not_traversed)


def levelOrder(root):
    nodes_not_traversed = []
    process_tree(root, nodes_not_traversed)





# Write your code here


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

levelOrder(tree.root)