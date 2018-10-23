class Solution(object):
    def bsearch(self, nums, target, lo=0, hi=None):
        hi = hi or len(nums) - 1
        while lo < hi:
            mid = (lo + hi) / 2
            if nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        if lo >= len(nums) or nums[lo] != target:
            return -1
        return lo

    def find_pivot(self, nums):
        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = (lo + hi) / 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        i = self.find_pivot(nums)
        # print 'pivot  ', i
        arr1_res = self.bsearch(nums, target, hi=i)
        arr2_res = self.bsearch(nums, target, lo=i)
        if arr1_res >= 0:
            return arr1_res
        return arr2_res


print Solution().search([4, 5, 6, 7, 0, 1, 2], 0), 4
print Solution().search([4, 5, 6, 7, 0, 1, 2], 3), -1
print Solution().search([4, 5, 6, 7, 0, 1, 2], 9), -1
print Solution().search([1], 9), -1
print Solution().search([1], 1), 0
print Solution().search([1], 0), -1
print Solution().search([1, 3], 3), 1
print Solution().search([1, 3], 1), 0
print Solution().search([1, 3], 0), -1
print Solution().search([3, 1], 1), 1
print Solution().search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19], 12)
