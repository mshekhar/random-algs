class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        start = None
        i = 0
        while i < len(nums) - 1 and nums[i] <= nums[i + 1]:
            i += 1
        if i == len(nums) - 1:
            return 0

        start = i
        end = None
        i = len(nums) - 1
        while i > start and nums[i - 1] <= nums[i] and nums[i] >= nums[start]:
            i -= 1
        end = i

        if start >= end:
            return 0

        i = start
        max_in_window = float('-inf')
        min_in_window = float('inf')
        while i <= end:
            max_in_window = max(max_in_window, nums[i])
            min_in_window = min(min_in_window, nums[i])
            i += 1

        # print start, end, nums[start], nums[end], min_in_window, max_in_window
        while start >= 0 and min_in_window < nums[start]:
            # print 'smaller than ', min_in_window, nums[start]
            start -= 1
        while end < len(nums) and nums[end] < max_in_window:
            # print 'greater than ', max_in_window, nums[end]
            end += 1
        # print start, end, nums[start], nums[end]
        return end - 1 - (start + 1) + 1


print Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15])
print Solution().findUnsortedSubarray([2, 4, 8, 15, 9, 10, 11, 12])
print Solution().findUnsortedSubarray([2, 6, 8, 10, 15])
print Solution().findUnsortedSubarray([2, 6, 8, 10, 9])
print Solution().findUnsortedSubarray([2, 3, 3, 2, 4])
