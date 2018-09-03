class Solution(object):
    def helper(self, nums, visited, start_idx, k, running_sum, target):
        if k == 1:
            return True

        if running_sum == target:
            return self.helper(nums, visited, 0, k - 1, 0, target)

        if running_sum > target:
            return False

        for i in range(start_idx, len(nums)):
            if not visited[i]:
                visited[i] = 1
                if self.helper(nums, visited, i + 1, k, running_sum + nums[i], target):
                    return True
                visited[i] = 0
        return False

    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        sum_nums = sum(nums)
        if sum_nums <= 0 or k <= 0 or sum_nums % k:
            return False
        return self.helper(nums, [0] * len(nums), 0, k, 0, sum_nums / k)


print Solution().canPartitionKSubsets([4, 3, 2, 3, 5, 2, 1], 4)
print Solution().canPartitionKSubsets([3, 2, 3, 5, 1], 4)
print Solution().canPartitionKSubsets([-1, 1, 0, 0], 4)
print Solution().canPartitionKSubsets([-1, 1], 1)
print Solution().canPartitionKSubsets([-1, 1], 2)
print Solution().canPartitionKSubsets([-1, 1, 0], 2)
