from Queue import Queue


class Solution(object):
    def __init__(self):
        self.graph_map = {}
        self.idx_map = {}

    def get_path_key(self, n1, n2):
        return str(min(n1, n2)) + "_" + str(max(n1, n2))

    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """

        self.graph_map = {c: l for c, l in enumerate(graph)}
        self.idx_map = {c: 0 for c in self.graph_map}

        q = Queue()
        q.put(0, [], set())
        while q.qsize() > 0:
            node, path, uniq_path = q.get()
            for n in self.graph_map[node]:
                q.put(n, path.append(node), uniq_path.add(node))


print Solution().shortestPathLength([[1, 2, 3], [0], [0], [0]])
print Solution().shortestPathLength([[1], [0, 2, 4], [1, 3, 4], [2], [1, 2]])
