#!/bin/python


#
# Complete the 'connectedCities' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER g
#  3. INTEGER_ARRAY originCities
#  4. INTEGER_ARRAY destinationCities
#


class DisjointSetNode(object):
    def __init__(self, data):
        self.data = data
        self.rank = 0
        self.parent = self


class DisjointSet(object):
    def __init__(self):
        self.node_data_map = {}

    def find_root(self, node):
        if not isinstance(node, DisjointSetNode):
            node = self.node_data_map.get(node) or DisjointSetNode(node)
        curr = node
        parent = curr.parent
        while parent != curr:
            curr = parent.parent
            parent = curr.parent
        return curr

    def union(self, data_1, data_2):
        if data_1 not in self.node_data_map:
            self.node_data_map[data_1] = DisjointSetNode(data_1)
        if data_2 not in self.node_data_map:
            self.node_data_map[data_2] = DisjointSetNode(data_2)
        node_1 = self.node_data_map[data_1]
        node_2 = self.node_data_map[data_2]

        root_1 = self.find_root(node_1)
        root_2 = self.find_root(node_2)

        if root_1 == root_2:
            return False

        if root_1.rank >= root_2.rank:
            root_2.parent = root_1
            if root_1.rank == root_2.rank:
                root_1.rank += 1
        else:
            root_1.parent = root_2
        return True


def connectedCities(n, g, originCities, destinationCities):
    ds = DisjointSet()
    for i in xrange(g + 1, n):
        x = 2
        if i not in ds.node_data_map:
            ds.node_data_map[i] = DisjointSetNode(i)

        while i * x <= n:
            if i * x not in ds.node_data_map:
                ds.node_data_map[i * x] = DisjointSetNode(i * x)
            # make root of i*x equal to root of i.
            ds.union(i, i * x)
            x += 1

    res = []
    for i in xrange(len(originCities)):
        origin = originCities[i]
        destination = destinationCities[i]
        if origin in ds.node_data_map and destination in ds.node_data_map:
            root_1 = ds.find_root(ds.node_data_map[origin])
            root_2 = ds.find_root(ds.node_data_map[destination])
            if root_1 == root_2:
                res.append(1)
            else:
                res.append(0)
        else:
            res.append(0)
    return res


if __name__ == '__main__':
    # print connectedCities(6, 2, [1, 2, 3], [4, 5, 6])
    # print connectedCities(6, 0, [1, 4, 3, 6], [3, 6, 2, 5])
    # print connectedCities(1, 1, [1], [2])
    print connectedCities(6, 1, [1, 2, 4, 6], [3, 3, 3, 4])
    print connectedCities(10, 1, [10, 4, 3, 6], [3, 6, 2, 9])
