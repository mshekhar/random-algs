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
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        candidates = []
        parents_map = {}
        for edge in edges:
            if edge[1] not in parents_map:
                parents_map[edge[1]] = edge[0]
            else:
                candidates = [[edge[0], edge[1]], [parents_map[edge[1]], edge[1]]]
                break

        # candidates.reverse()
        if candidates:
            # print candidates
            for c in [0, 1]:
                ds = DisjointSet()
                for edge in edges:
                    node_1, node_2 = edge
                    if edge == candidates[c]:
                        continue
                    if not ds.union(node_1, node_2):
                        return candidates[c ^ 1]
                return candidates[c]

        else:
            res = [None, None]
            ds = DisjointSet()
            for data_1, data_2 in edges:
                if not ds.union(data_1, data_2):
                    res = [data_1, data_2]
            return res


print Solution().findRedundantDirectedConnection([[4, 2], [1, 5], [5, 2], [5, 3], [2, 4]])
print Solution().findRedundantDirectedConnection([[4, 2]])
print Solution().findRedundantDirectedConnection([])
print Solution().findRedundantDirectedConnection([[1, 2], [1, 3], [2, 3]])
print Solution().findRedundantDirectedConnection([[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]])
