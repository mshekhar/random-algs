class CycleException(Exception):
    pass


class Solution(object):
    def topologicalSortUtil(self, node_label, visited, stack, directed_graph):
        visited[node_label] = -1
        for nei in directed_graph[node_label]:
            if not visited[nei]:
                self.topologicalSortUtil(nei, visited, stack, directed_graph)
            elif visited[nei] == -1:
                raise CycleException("cycle {0} and {1}".format(str(node_label), str(nei)))
        visited[node_label] = 1
        stack.insert(0, node_label)

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        try:
            directed_graph = []
            visited = []
            stack = []
            for _ in xrange(numCourses):
                directed_graph.append([])
                visited.append(0)

            for req, pre_req in prerequisites:
                directed_graph[pre_req].append(req)

            for node_label in xrange(numCourses):
                if not visited[node_label]:
                    self.topologicalSortUtil(node_label, visited, stack, directed_graph)

            # print stack
            return stack
        except CycleException as e:
            # print 'cycle', e
            return []

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        return self.canFinish(numCourses, prerequisites)


print Solution().findOrder(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])
print Solution().findOrder(2, [[1, 0], [0, 1]])
print Solution().findOrder(2, [[1, 0]])
print Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]])
