class Solution(object):
    def helper(self, nums, target, idx, dp):
        if target in dp:
            return dp[target]

        res = 0
        for i in range(idx, len(nums)):
            # print nums[i], target, res
            if not nums[i]:
                continue
            if nums[i] < target:
                res += self.helper(nums, target - nums[i], idx, dp)
            elif nums[i] == target:
                res += 1
        dp[target] = res
        return dp[target]

    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = {}
        res = self.helper(nums, target, 0, {})
        # print dp
        return res


print Solution().combinationSum4([5], 4)
