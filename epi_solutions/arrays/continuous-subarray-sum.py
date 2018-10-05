class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        subarray_map = {0: -1}
        sums = 0
        for c, n in enumerate(nums):
            sums += n
            if k:
                sums %= k
            if sums in subarray_map:
                if c - subarray_map[sums] > 1:
                    return True
            else:
                subarray_map[sums] = c
        return False


print Solution().checkSubarraySum([1, 2, 3, 0], 0)
print Solution().checkSubarraySum([0, 1, 0, 0], 0)
