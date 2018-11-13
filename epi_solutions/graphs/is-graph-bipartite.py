class Solution(object):
    def is_valid_color(self, node, graph, colors, new_color):
        if colors[node] != 0:
            return colors[node] == new_color
        colors[node] = new_color
        for next_node in graph[node]:
            if not self.is_valid_color(next_node, graph, colors, -1 * new_color):
                return False
        return True

    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        node_count = len(graph)
        colors = [0] * node_count
        for node in xrange(node_count):
            if colors[node] == 0 and not self.is_valid_color(node, graph, colors, 1):
                return False
        return True


print Solution().isBipartite([[1, 3], [0, 2], [1, 3], [0, 2]])
print Solution().isBipartite([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]])
