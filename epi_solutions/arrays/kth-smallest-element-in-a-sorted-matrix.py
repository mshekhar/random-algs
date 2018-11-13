import heapq


class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        min_heap = []
        for i in xrange(m):
            heapq.heappush(min_heap, (matrix[i][0], i, 0))

        i = 0
        while i < k:
            val, x, y = heapq.heappop(min_heap)
            if y + 1 < n:
                heapq.heappush(min_heap, (matrix[x][y + 1], x, y + 1))
            i += 1
        return val


print Solution().kthSmallest([
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
], 8)
