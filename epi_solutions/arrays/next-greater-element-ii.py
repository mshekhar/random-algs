class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        stack = []
        res = [None] * len(nums)
        for i in xrange(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                idx = stack.pop()
                res[idx] = nums[i]
            stack.append(i)

        if stack:
            for i in xrange(len(nums)):
                while stack and nums[stack[-1]] < nums[i]:
                    idx = stack.pop()
                    res[idx] = nums[i]
                while stack and stack[-1] <= i:
                    idx = stack.pop()
                    res[idx] = -1
                if res[i] is None:
                    stack.append(i)
        return res


print Solution().nextGreaterElements([1, 2, 1])
print Solution().nextGreaterElements([10, 1, 1])
print Solution().nextGreaterElements([1, 2, 1, 5, 1, 0, 2, 1])
print Solution().nextGreaterElements([1])
print Solution().nextGreaterElements([1, 1, 1, 1, 1])
