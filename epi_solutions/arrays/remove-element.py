class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        non_val_i = 0
        while i < len(nums):
            if nums[i] != val:
                nums[non_val_i] = nums[i]
                non_val_i += 1
            i += 1

        # while len(nums) != non_val_i:
        #     nums.pop()
        return non_val_i


def solve(arr, val):
    print arr, val
    print Solution().removeElement(arr, val), arr


solve([0, 1, 2, 2, 3, 0, 4, 2], 2)
solve([3, 2, 2, 3], 2)
solve([3, 2, 2, 3], 3)
solve([3, 2, 2, 3], 1)
