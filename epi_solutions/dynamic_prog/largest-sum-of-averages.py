class Solution(object):
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """

        sums = [0]
        for i in A:
            sums.append(sums[-1] + i)
        average = lambda x, y: (sums[y] - sums[x]) * 1.0 / (y - x)
        dp = [average(i, len(A)) for i, _ in enumerate(A)]
        for k in xrange(K - 1):
            for i in xrange(len(A)):
                for j in xrange(i + 1, len(A)):
                    dp[i] = max(dp[i], average(i, j) + dp[j])
        return dp[0]


Solution().largestSumOfAverages([9, 1, 2, 3, 9], 3)
