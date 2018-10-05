class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        stack = []
        if len(nums) < 3:
            return False
        mins = [nums[0]]
        for i in range(1, len(nums)):
            mins.append(min(mins[-1], nums[i]))
        # print mins
        curr = len(nums) - 1
        while curr >= 0:
            if nums[curr] > mins[curr]:
                while stack and stack[-1] <= mins[curr]:
                    stack.pop()
                if stack and stack[-1] < nums[curr]:
                    return True
                stack.append(nums[curr])
            curr -= 1
        return False


print Solution().find132pattern([1, 2, 3, 4])
print Solution().find132pattern([3, 1, 4, 2])
print Solution().find132pattern([-1, 3, 2, 0])
print Solution().find132pattern([3, 5, 0, 3, 4])
