class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        try:
            m = len(grid)
            n = len(grid[0])
            if not m or not n:
                return 0
        except:
            return 0
        dp = [[0 for _ in xrange(n)] for _ in xrange(m)]
        for i in xrange(m):
            counter = 0
            for j in xrange(n):
                if grid[i][j] == 'E':
                    counter += 1
                elif grid[i][j] == 'W':
                    counter = 0
                else:
                    dp[i][j] += counter

            counter = 0
            for j in xrange(n - 1, -1, -1):
                if grid[i][j] == 'E':
                    counter += 1
                elif grid[i][j] == 'W':
                    counter = 0
                else:
                    dp[i][j] += counter
        max_ele = 0
        for j in xrange(n):
            counter = 0
            for i in xrange(m):
                if grid[i][j] == 'E':
                    counter += 1
                elif grid[i][j] == 'W':
                    counter = 0
                else:
                    dp[i][j] += counter

            counter = 0
            for i in xrange(m - 1, -1, -1):
                if grid[i][j] == 'E':
                    counter += 1
                elif grid[i][j] == 'W':
                    counter = 0
                else:
                    dp[i][j] += counter
                    max_ele = max(max_ele, dp[i][j])

        # for row in dp:
        #     print row
        return max_ele


print Solution().maxKilledEnemies([["0", "E", "0", "0"],
                                   ["E", "0", "W", "E"],
                                   ["0", "E", "0", "0"]])
print Solution().maxKilledEnemies([[]])
print Solution().maxKilledEnemies([])
print Solution().maxKilledEnemies(["E"])
