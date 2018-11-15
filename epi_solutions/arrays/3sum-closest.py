class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = float('inf')
        nums.sort()
        for i in xrange(len(nums) - 2):
            start = i + 1
            end = len(nums) - 1
            while start < end:
                curr_sum = nums[i] + nums[start] + nums[end]
                if curr_sum > target:
                    end -= 1
                elif curr_sum < target:
                    start += 1
                else:
                    return curr_sum
                if abs(target - result) > abs(target - curr_sum):
                    result = curr_sum
        return result


print Solution().threeSumClosest([-1, 2, 1, -4], 1)
print Solution().threeSumClosest([-1], 1)
print Solution().threeSumClosest([0, 1, 2], 3)
