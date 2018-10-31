class Solution(object):
    # counter = {}

    def helper(self, row, col, m, n, dp):
        if row < 0 or col < 0 or row >= m or col >= n:
            return 0
        if row == m - 1 and col == n - 1:
            return 1
        if (row, col) in dp:
            return dp[(row, col)]
        # if (row, col) not in self.counter:
        #     self.counter[(row, col)] = 0
        # self.counter[(row, col)] += 1
        dp[(row, col)] = -1
        res = 0
        for new_row, new_col in [(row + 1, col), (row, col + 1)]:
            if dp.get((new_row, new_col), None) != -1:
                tmp = self.helper(new_row, new_col, m, n, dp)
                # if tmp > 0:
                #     print row, col, new_row, new_col, tmp
                res += tmp
        dp[(row, col)] = res
        return dp[(row, col)]

    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        if m < 1 or n < 1:
            return 0
        return self.helper(0, 0, m, n, {})


print Solution().uniquePaths(3, 2)
print Solution().uniquePaths(7, 3)
print Solution().uniquePaths(1, 1)
print Solution().uniquePaths(23, 12)
