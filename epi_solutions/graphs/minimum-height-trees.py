class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n > 0 and not edges:
            return [0]
        graph = [set() for _ in xrange(n)]
        for i, j in edges:
            graph[i].add(j)
            graph[j].add(i)

        deg_one_nodes = [i for i in xrange(n) if len(graph[i]) == 1]
        while n > 2:
            n -= len(deg_one_nodes)
            new_deg_one_nodes = []
            for i in deg_one_nodes:
                j = graph[i].pop()
                graph[j].remove(i)
                if len(graph[j]) == 1:
                    new_deg_one_nodes.append(j)
            deg_one_nodes = new_deg_one_nodes
        return deg_one_nodes
