class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        max_reach = 0
        for c, i in enumerate(nums):
            if i == 0 and c != len(nums) - 1 and max_reach <= c:
                return False
            max_reach = max(max_reach, c + i)
        return True


print Solution().canJump([2, 3, 1, 1, 4])
print Solution().canJump([3, 2, 1, 0, 4])
print Solution().canJump([3, 2, 1, 0])
print Solution().canJump([])
print Solution().canJump([0])
print Solution().canJump([0, 1])
