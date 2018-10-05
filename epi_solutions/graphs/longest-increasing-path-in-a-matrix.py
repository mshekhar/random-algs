class CycleException(Exception):
    pass


class Solution(object):
    def construct_graph(self, m, n, matrix):
        graph = {}
        for i in xrange(m):
            for j in xrange(n):
                graph[(i, j)] = []
                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if x < 0 or y < 0 or x >= m or y >= n:
                        continue
                    if matrix[i][j] > matrix[x][y]:
                        graph[(i, j)].append((x, y))
        return graph

    def topological_sort(self, x, y, visited, graph, matrix):
        visited[(x, y)] = 0
        tmp_max = 0
        for nx, ny in graph[(x, y)]:
            if not visited.get((nx, ny)):
                self.topological_sort(nx, ny, visited, graph, matrix)
            tmp_max = max(visited[(nx, ny)], tmp_max)
            # print (x, y), (nx, ny), matrix[x][y], matrix[nx][ny], visited[(x, y)], visited[(nx, ny)], tmp_max
        visited[(x, y)] = 1 + tmp_max
        # print 'end loop', (x, y), visited[(x, y)]

    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        try:
            m = len(matrix)
            n = len(matrix[0])
            if m < 1 or n < 1:
                return 0
            graph = self.construct_graph(m, n, matrix)
            # print graph
            visited = {}
            max_stack_len = 0

            for x, y in graph:
                if not visited.get((x, y)):
                    self.topological_sort(x, y, visited, graph, matrix)
                max_stack_len = max(visited[(x, y)], max_stack_len)
            return max_stack_len
        except (CycleException, IndexError) as e:
            # print 'cycle', e
            return 0


print Solution().longestIncreasingPath([
    [9, 9, 4],
    [6, 6, 8],
    [2, 1, 1]
])

print Solution().longestIncreasingPath([
    [3, 4, 5],
    [3, 2, 6],
    [2, 2, 1]
])
