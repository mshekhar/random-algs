class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) / 2
            mid_next = mid + 1
            if nums[mid] > nums[mid_next]:
                high = mid
            else:
                low = mid_next
        return low


print Solution().findPeakElement([1, 2, 3, 1])
