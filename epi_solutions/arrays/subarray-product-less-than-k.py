class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        i = 0
        j = 0

        p = 1
        res = 0
        while i < len(nums):
            p *= nums[i]
            while p >= k and j <= i:
                p /= nums[j]
                j += 1
            i += 1
            res += i - j

        return res


print Solution().numSubarrayProductLessThanK([10, 5, 2, 6], 100)
print Solution().numSubarrayProductLessThanK([1, 2, 3], 0)
