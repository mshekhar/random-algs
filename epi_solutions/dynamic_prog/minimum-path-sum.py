class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        dp = []
        col_sum = None
        for i in range(len(grid)):
            tmp = []
            if not i:
                s = 0
                for j in range(len(grid[i])):
                    s += grid[i][j]
                    tmp.append(s)
            else:
                for j in range(len(grid[i])):
                    if not j:
                        if not col_sum:
                            col_sum = grid[i - 1][j]
                        col_sum += grid[i][j]
                        tmp.append(col_sum)
                    else:
                        tmp.append(0)
            dp.append(tmp)

        # print dp
        for i in range(1, len(grid)):
            for j in range(1, len(grid[i])):
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
                # print i, j, dp[i - 1][j], dp[i][j - 1], grid[i][j], dp[i][j]
        # print grid
        # print dp
        try:
            return dp[-1][-1]
        except IndexError:
            return 0


print Solution().minPathSum([
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
])
print Solution().minPathSum([])
print Solution().minPathSum([[1, 2], [1, 1]])
