class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        if not nums:
            return
        counters = [0, 0, 0]
        for i in nums:
            counters[i] += 1
        c = 0
        for i in [0, 1, 2]:
            for _ in xrange(counters[i]):
                nums[c] = i
                c += 1


nums = [2, 0, 2, 1, 1, 0]
print nums
Solution().sortColors(nums)
print nums
