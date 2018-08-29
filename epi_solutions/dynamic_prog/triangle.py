class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        if not triangle:
            return 0
        dp = triangle[-1]
        for h in range(len(triangle) - 2, -1, -1):
            for i in range(len(triangle[h])):
                # print len(dp), i, h, triangle[h][i], min(dp[i], dp[i + 1]), min(dp[i], dp[i + 1]) + triangle[h][i]
                dp[i] = min(dp[i], dp[i + 1]) + triangle[h][i]
        if dp:
            return dp[0]
        return 0


print Solution().minimumTotal([
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
])
print Solution().minimumTotal([[1]])
print Solution().minimumTotal([[-1], [-2, -3]])
