class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """

        sums = [0]
        for i in nums:
            sums.append(sums[-1] + i)
        range_sum = lambda x, y: sums[y] - sums[x]
        dp = [range_sum(i, len(nums)) for i, _ in enumerate(nums)]
        print dp
        for k in xrange(m - 1):
            for i in xrange(len(nums)):
                for j in xrange(i + 1, len(nums)):
                    dp[i] = min(dp[i], range_sum(i, j) + dp[j])
        print dp
        return dp[0]


print Solution().splitArray([7, 2, 5, 10, 8], 2)
