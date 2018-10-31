class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in nums:
            num = abs(i)
            if nums[num - 1] < 0:
                res.append(num)
            nums[num - 1] = -abs(nums[num - 1])
        return res


print Solution().findDuplicates([4, 3, 2, 7, 8, 2, 3, 1])
