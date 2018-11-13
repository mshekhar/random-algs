import collections


class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        edge_counter = collections.Counter()
        max_edge_count = 0
        for i in xrange(len(wall)):
            edge_end = 0
            for j in xrange(len(wall[i]) - 1):
                edge_end += wall[i][j]
                # print edge_end
                edge_counter[edge_end] += 1
                max_edge_count = max(max_edge_count, edge_counter[edge_end])
        # print edge_counter
        return len(wall) - max_edge_count


print Solution().leastBricks([[1, 2, 2, 1],
                              [3, 1, 2],
                              [1, 3, 2],
                              [2, 4],
                              [3, 1, 2],
                              [1, 3, 1, 1]])
