import collections
from Queue import Queue


class Solution(object):
    def construct_graph(self, seqs):
        graph = {}
        for seq in seqs:
            i = 0
            while i < len(seq):
                if seq[i] not in graph:
                    graph[seq[i]] = set()
                if i + 1 < len(seq) and seq[i] != seq[i + 1]:
                    graph[seq[i]].add(seq[i + 1])
                i += 1
        return graph

    def topological_sort(self, graph):
        in_degrees = collections.Counter()

        for i in graph:
            for j in graph[i]:
                in_degrees[j] += 1
        queue = Queue()
        for i in graph:
            if in_degrees[i] == 0:
                queue.put(i)
                if queue.qsize() > 1:
                    return []

        topological_order = []
        while queue.qsize() > 0:
            node = queue.get()
            topological_order.append(node)
            for i in graph[node]:
                in_degrees[i] -= 1
                if in_degrees[i] == 0:
                    queue.put(i)
                    if queue.qsize() > 1:
                        return []
        return topological_order

    def sequenceReconstruction(self, org, seqs):
        """
        :type org: List[int]
        :type seqs: List[List[int]]
        :rtype: bool
        """
        graph = self.construct_graph(seqs)
        topological_order = self.topological_sort(graph)
        if topological_order == org:
            return True
        return False


print Solution().sequenceReconstruction([1, 2, 3], [[1, 2], [1, 3]])
print Solution().sequenceReconstruction([1, 2, 3], [[1, 2]])
print Solution().sequenceReconstruction([1, 2, 3], [[1, 2], [1, 3], [2, 3]])
print Solution().sequenceReconstruction([4, 1, 5, 2, 6, 3], [[5, 2, 6, 3], [4, 1, 5, 2]])
print Solution().sequenceReconstruction(1, [1, 1])
