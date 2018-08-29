class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        if not nums:
            return []
        nums = sorted(nums)
        path_tracker = []
        largest_div_dp = []
        for i in range(len(nums)):
            largest_div_dp.append(1)
            path_tracker.append(-1)
            for j in range(i - 1, -1, -1):
                if not nums[i] % nums[j]:
                    if largest_div_dp[j] + 1 > largest_div_dp[i]:
                        largest_div_dp[i] = largest_div_dp[j] + 1
                        path_tracker[i] = j

        sol = []
        max_path_idx = largest_div_dp.index(max(largest_div_dp))
        # print max_path_idx
        # print largest_div_dp
        # print path_tracker
        index = max_path_idx
        while index >= 0:
            # print index, sol
            sol.insert(0, nums[index])
            index = path_tracker[index]
        return sol


print Solution().largestDivisibleSubset([1, 2, 3])
print Solution().largestDivisibleSubset([1])
print Solution().largestDivisibleSubset([1, 2, 4, 8])
