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


class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        ds = DisjointSet()
        for i in xrange(len(M)):
            ds.node_data_map[i] = ds.node_data_map.get(i) or DisjointSetNode(i)
            for j in xrange(i + 1, len(M)):
                if M[i][j] == 1:
                    _ = ds.union(i, j)
        res = set()
        for i in xrange(len(M)):
            res.add(ds.find_root(ds.node_data_map[i]).data)
        return len(res)


print Solution().findCircleNum([[1, 1, 0],
                                [1, 1, 1],
                                [0, 1, 1]])
print Solution().findCircleNum([[1, 1, 0],
                                [1, 1, 0],
                                [0, 0, 1]])
