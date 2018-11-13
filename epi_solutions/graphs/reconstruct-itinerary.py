class Solution(object):
    def topologicalSortUtil(self, node, stack, directed_graph):
        while directed_graph.get(node, []):
            nei = directed_graph[node].pop()
            self.topologicalSortUtil(nei, stack, directed_graph)
        stack.append(node)

    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """

        directed_graph = {}
        for origin, dest in tickets:
            directed_graph.setdefault(origin, []).append(dest)

        for node in directed_graph:
            directed_graph[node].sort(reverse=True)

        stack = []

        # print directed_graph, stack
        self.topologicalSortUtil("JFK", stack, directed_graph)
        return stack[::-1]


print Solution().findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]])
print Solution().findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]])
