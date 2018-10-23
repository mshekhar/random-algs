class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        p = 1
        res = []
        for i in xrange(len(nums)):
            res.append(p)
            p *= nums[i]

        p = 1
        for i in xrange(len(nums) - 1, -1, -1):
            res[i] *= p
            p *= nums[i]

        return res


print Solution().productExceptSelf([1, 2, 3, 4])
print Solution().productExceptSelf([])
