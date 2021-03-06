

def processTree(root, tree):
    if root.left:
        processTree(root.left, tree)

    print(root.data)

    if root.right:
        processTree(root.right, tree)


def inOrderTraversal(root):
    tree = []
    processTree(root, tree)
    return tree


def check_binary_search_tree_(root):
    tree = inOrderTraversal(root)

    for index, element in enumerate(tree):
        for j in range(index+1, len(tree)):
            if element == tree[j]:
                return False

    if tree == sorted(tree):
        return True
    else:
        return False
