class disjoint_Set:
    class Node:
        def __init__(self, data):
            self.value = data
            self.parent = self
            self.rank = 0

    def __init__(self):
        self.dic = {}

    def make_set(self, data):
        if data not in self.dic:
            self.dic[data] = self.Node(data)
        return self.dic

    def find_set(self, data):  # parent of a node represents the set in our algo
        if data in self.dic:
            node = self.dic[data]
        else:
            return False

        if node.parent == node:
            return node

        node.parent = self.find_set(node.parent.value)
        return node.parent

    def union_set(self, vertice1, vertice2):
        node1 = self.find_set(vertice1)
        node2 = self.find_set(vertice2)

        if node1 and node2 and node1 != node2:
            if node1.rank >= node2.rank:
                if node1.rank == node2.rank:
                    node1.rank += 1
                node2.parent = node1
            else:
                node1.parent = node2

        return True


if __name__ == '__main__':
    n = int(input())

    output = [0] * (n + 1)

    DisjointSet = disjoint_Set()

    for _ in range(n):
        ver1, ver2 = [int(x) for x in input().strip().split()]

        DisjointSet.make_set(ver1)
        DisjointSet.make_set(ver2)

        DisjointSet.union_set(ver1, ver2)
    for element in DisjointSet.dic.keys():
        output[DisjointSet.find_set(element).value] += 1

    dset_max = max(output)
    dset_min = min(filter(lambda x: x > 0, output))

    print("{} {}".format(dset_min, dset_max))