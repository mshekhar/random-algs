import heapq


class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        min_heap = []
        seen = set()
        seen.add((0, 0))
        if not grid or not grid[0]:
            return 0
        heapq.heappush(min_heap, (grid[0][0], 0, 0))
        res = 0
        while min_heap:
            elevation, i, j = heapq.heappop(min_heap)
            # print elevation, i, j, min_heap, len(grid)
            res = max(res, elevation)
            if i == len(grid) - 1 and j == len(grid) - 1:
                return res
            for x, y in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                if 0 <= x < len(grid) and 0 <= y < len(grid) and (x, y) not in seen:
                    seen.add((x, y))
                    # print x, y
                    heapq.heappush(min_heap, (grid[x][y], x, y))
        return 0


print Solution().swimInWater([[0, 2], [1, 3]])
print Solution().swimInWater([[0]])
print Solution().swimInWater([[]])
print Solution().swimInWater([[0, 1, 2, 3, 4],
                              [24, 23, 22, 21, 5],
                              [12, 13, 14, 15, 16],
                              [11, 17, 18, 19, 20],
                              [10, 9, 8, 7, 6]])
