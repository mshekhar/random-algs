import heapq


class HeapObject(object):
    def __init__(self, x, y, height):
        self.x = x
        self.y = y
        self.height = height

    def __cmp__(self, other):
        return cmp(self.height, other.height)


class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """

        min_heap = []
        try:
            m = len(heightMap)
            n = len(heightMap[0])
            if not m or not n:
                return 0
        except:
            return 0
        visited = [[False for _ in xrange(n)] for _ in xrange(m)]
        for i in [0, m - 1]:
            for j in xrange(n):
                heapq.heappush(min_heap, HeapObject(height=heightMap[i][j], x=i, y=j))
                visited[i][j] = True

        for j in [0, n - 1]:
            for i in xrange(m):
                heapq.heappush(min_heap, HeapObject(height=heightMap[i][j], x=i, y=j))
                visited[i][j] = True

        next_pos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        total_water = 0
        while min_heap:
            ho = heapq.heappop(min_heap)
            for np in next_pos:
                row_new = ho.x + np[0]
                col_new = ho.y + np[1]

                if 0 <= row_new < m and 0 <= col_new < n and not visited[row_new][col_new]:
                    if ho.height > heightMap[row_new][col_new]:
                        total_water += ho.height - heightMap[row_new][col_new]
                    visited[row_new][col_new] = True
                    heapq.heappush(min_heap, HeapObject(height=max(ho.height, heightMap[row_new][col_new]),
                                                        x=row_new, y=col_new))
        return total_water

try:
    print Solution().trapRainWater([
        [1, 4, 3, 1, 3, 2],
        [3, 2, 1, 3, 2, 4],
        [2, 3, 3, 2, 3, 1]
    ])
except:
    import time
    time.sleep(0.2)
    raise
