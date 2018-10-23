class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        j = 0
        running_sum = 0
        res = float('inf')
        res_indices = []
        while i < len(nums) and j < len(nums):
            while i < len(nums) and running_sum < s:
                running_sum += nums[i]
                i += 1
                # print running_sum, i, s, j

                if running_sum >= s and i - j < res:
                    res = i - j
                    res_indices = [j, i]

            while j < len(nums) and running_sum >= s and j <= i:
                running_sum -= nums[j]
                j += 1
                if running_sum >= s and i - j < res:
                    res = i - j
                    res_indices = [j, i]
            # print 'two', running_sum, i, s, j
        # print res_indices
        return 0 if not res_indices else res


print Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
print Solution().minSubArrayLen(7, [2, 3, 1, 2, 4, 3, 8])
print Solution().minSubArrayLen(70, [2, 3, 1, 2, 4, 3, 8])
print Solution().minSubArrayLen(70, [])
print Solution().minSubArrayLen(7, [2, 3, 1, 1])
