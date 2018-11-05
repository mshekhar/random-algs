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

    @classmethod
    def runner(cls):
        ds = DisjointSet()

        print ds.union(1, 2)
        print map(lambda x: (x.data, x.rank, ds.find_root(x).data), ds.node_data_map.values())
        print ds.union(2, 3)
        print map(lambda x: (x.data, x.rank, ds.find_root(x).data), ds.node_data_map.values())
        print ds.union(4, 5)
        print map(lambda x: (x.data, x.rank, ds.find_root(x).data), ds.node_data_map.values())
        print ds.union(6, 7)
        print map(lambda x: (x.data, x.rank, ds.find_root(x).data), ds.node_data_map.values())
        print ds.union(5, 6)
        print map(lambda x: (x.data, x.rank, ds.find_root(x).data), ds.node_data_map.values())
        print ds.union(3, 7)
        print map(lambda x: (x.data, x.rank, ds.find_root(x).data), ds.node_data_map.values())
        print ds.union(2, 5)
        print map(lambda x: (x.data, x.rank, ds.find_root(x).data), ds.node_data_map.values())

        print ds.find_root(1).data
        print ds.find_root(2).data
        print ds.find_root(3).data
        print ds.find_root(4).data
        print ds.find_root(5).data
        print ds.find_root(6).data
        print ds.find_root(7).data


class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        res = [None, None]
        ds = DisjointSet()
        for data_1, data_2 in edges:
            if not ds.union(data_1, data_2):
                res = [data_1, data_2]
        return res


print Solution().findRedundantConnection([[1, 2], [1, 3], [2, 3]])
print Solution().findRedundantConnection([[1, 2], [1, 3]])
print Solution().findRedundantConnection([[1, 2]])
print Solution().findRedundantConnection([])
print Solution().findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]])
