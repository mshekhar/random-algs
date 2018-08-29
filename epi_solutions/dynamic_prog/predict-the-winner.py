class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        dp = [[0 for _ in xrange(len(nums))] for _ in xrange(len(nums))]
        for i in xrange(len(nums)):
            dp[i][i] = nums[i]

        for l in xrange(1, len(nums)):
            for i in xrange(0, len(nums) - l):
                j = l + i
                dp[i][j] = max(nums[i] - dp[i + 1][j], nums[j] - dp[i][j - 1])

        return dp[0][len(nums) - 1] >= 0


print Solution().PredictTheWinner([1, 5, 2])
print Solution().PredictTheWinner([1, 5, 233, 7])
