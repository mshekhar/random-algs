class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        i = 0
        non_zero_i = 0
        while i < len(nums):
            if nums[i] != 0:
                nums[non_zero_i] = nums[i]
                non_zero_i += 1
            i += 1

        while non_zero_i < len(nums):
            nums[non_zero_i] = 0
            non_zero_i += 1


def solve(arr):
    print arr
    Solution().moveZeroes(arr)
    print arr


solve([0, 1, 0, 3, 12])
solve([1, 3, 12])
solve([0, 0, 0])
solve([0, 1])
solve([1, 0])
solve([0])
solve([1])
solve([])
