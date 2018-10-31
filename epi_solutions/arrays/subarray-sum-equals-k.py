class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        running_sum = 0
        sum_map = {0: 1}
        res = 0
        for i in nums:
            running_sum += i
            if running_sum not in sum_map:
                sum_map[running_sum] = 0
            res += sum_map.get(running_sum - k, 0)
            sum_map[running_sum] += 1

        return res


print Solution().subarraySum([1, 1, 1, 1, 1], 2)
