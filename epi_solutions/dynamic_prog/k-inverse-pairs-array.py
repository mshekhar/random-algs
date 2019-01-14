class Solution(object):
    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """

        # dp[n][k + 1] = dp[n][k] + dp[n - 1][k + 1] - dp[n - 1][k + 1 - n]
        if k > n * (n - 1) / 2 or k < 0:
            return 0
        if k == 0 or k == n * (n - 1) / 2:
            return 1
        dp = [[0 for _ in xrange(k + 1)] for _ in xrange(n + 1)]
        dp[2][0] = 1
        dp[2][1] = 1
        for i in xrange(3, n + 1):
            dp[i][0] = 1
            for j in xrange(1, 1 + min(k, (i * (i - 1) / 2))):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
                if j >= i:
                    dp[i][j] -= dp[i - 1][j - i]
                dp[i][j] = (dp[i][j] + 1000000007) % 1000000007
        return dp[n][k]


print Solution().kInversePairs(10, 3)
