class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        difference_till_now = 0
        max_subarray = 0
        difference_cache = {0: -1}
        for c, i in enumerate(nums):
            difference_till_now += 1 if i == 1 else -1
            if difference_till_now in difference_cache:
                max_subarray = max(max_subarray, c - difference_cache[difference_till_now])
            else:
                difference_cache[difference_till_now] = c
            # print difference_till_now, difference_cache
        return max_subarray


print Solution().findMaxLength([0, 1])
print Solution().findMaxLength([1, 0, 1])
print Solution().findMaxLength([0, 0, 0, 0, 1, 1])
