class Solution(object):
    def helper(self, nums, target):
        dp_sum = [0] * (target + 1)
        dp_sum[0] = 1
        for j in nums:
            for i in range(target, j - 1, -1):
                dp_sum[i] += dp_sum[i - j]
        return dp_sum[-1]

    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """

        # sum(positives)+sum(negatives) = sum(nums)
        # sum(positives)-sum(negatives) = S
        # sum(positives) = (sum(nums) + S)/2
        arr_sum = sum(nums)
        target = (sum(nums) + S)
        if arr_sum < S or target % 2:
            return 0
        return self.helper(nums, target / 2)


print Solution().findTargetSumWays([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 0)
