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
    def are_strings_similar(self, str_1, str_2):
        diff = 0
        for i in xrange(len(str_1)):
            if str_1[i] != str_2[i]:
                diff += 1
                if diff > 2:
                    return False
        return True

    def numSimilarGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        ds = DisjointSet()
        for i in xrange(len(A)):
            ds.node_data_map[A[i]] = ds.node_data_map.get(A[i]) or DisjointSetNode(A[i])
            for j in xrange(i + 1, len(A)):
                if self.are_strings_similar(A[i], A[j]):
                    _ = ds.union(A[i], A[j])
        res = set()
        for i in A:
            res.add(ds.find_root(ds.node_data_map[i]).data)
        return len(res)


print Solution().numSimilarGroups(["tars", "rats", "arts", "star"])
