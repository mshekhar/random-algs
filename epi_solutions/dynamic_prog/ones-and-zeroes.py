class Solution(object):
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for _ in xrange(n + 1)] for _ in xrange(m + 1)]
        for s in strs:
            n_ones = 0
            n_zeros = 0
            for c in s:
                if c == '1':
                    n_ones += 1
                else:
                    n_zeros += 1

            for i in range(m, n_zeros - 1, -1):
                for j in range(n, n_ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - n_zeros][j - n_ones] + 1)

        return dp[-1][-1]


print Solution().findMaxForm(["10", "0001", "111001", "1", "0"], m=5, n=3)
print Solution().findMaxForm(["10", "1", "0"], m=1, n=1)
print Solution().findMaxForm(["110", "1", "0"], m=1, n=1)
