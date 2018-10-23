class Solution(object):
    def find_left(self, nums, target, lo=0, hi=None):
        if lo < 0:
            return -1
        hi = hi or len(nums)
        while lo < hi:
            mid = lo + ((hi - lo) / 2)
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def find_right(self, nums, target, lo=0, hi=None):
        if lo < 0:
            return -1
        hi = hi or len(nums)
        while lo < hi:
            mid = lo + ((hi - lo) / 2)
            if target < nums[mid]:
                hi = mid
            else:
                lo = mid + 1
        return lo

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        left = self.find_left(nums, target)
        right = self.find_right(nums, target) - 1
        if left > right:
            return [-1, -1]
        return [left if nums[left] == target else -1, right if right >= 0 and nums[right] == target else -1]


# print Solution().searchRange([5, 7, 7, 8, 8, 8, 10], 8)
# print Solution().searchRange([5, 7, 7, 8, 8, 8, 10], 6)
# print Solution().searchRange([], 0)
print Solution().searchRange([2, 2], 3)
print Solution().searchRange([2, 4], 2)
