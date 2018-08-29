class Solution(object):
    def helper(self, nums, target):
        dp_sum = [0] * (target + 1)
        dp_sum[0] = 1
        for j in nums:
            for i in range(target, j - 1, -1):
                dp_sum[i] += dp_sum[i - j]
        return dp_sum[-1]

    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        arr_sum = sum(nums)
        if not arr_sum or arr_sum % 2:
            return False
        return bool(self.helper(nums, arr_sum / 2))


print Solution().canPartition([1, 5, 11, 5])
print Solution().canPartition([1, 2, 3, 5])
