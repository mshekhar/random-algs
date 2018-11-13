class Solution(object):
    def is_node_safe(self, node, graph, colors):
        if colors[node] != 0:
            return colors[node] == 1

        colors[node] = 2
        for next_node in graph[node]:
            if not self.is_node_safe(next_node, graph, colors):
                return False
        colors[node] = 1
        return True

    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        if not graph:
            return []
        node_count = len(graph)
        colors = [0] * node_count
        res = []
        for node in xrange(node_count):
            if self.is_node_safe(node, graph, colors):
                res.append(node)
        return res
