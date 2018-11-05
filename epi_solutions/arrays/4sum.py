class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        self.helper(nums, 0, target, 4, [], res)
        return res

    def helper(self, nums, start, target, N, curr_res, res):
        if len(nums) < N or N < 2:
            return

        if N == 2:
            l = start
            r = len(nums) - 1
            while l < r:
                if nums[l] + nums[r] == target:
                    res.append(curr_res + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(start, len(nums) - N + 1):  # careful about range
                if target < nums[i] * N or target > nums[-1] * N:  # take advantages of sorted list
                    break
                if i == start or i > start and nums[i - 1] != nums[i]:  # recursively reduce N
                    self.helper(nums, i + 1, target - nums[i], N - 1, curr_res + [nums[i]], res)


print Solution().fourSum([1, 0, -1, 0, -2, 2], target=0)
