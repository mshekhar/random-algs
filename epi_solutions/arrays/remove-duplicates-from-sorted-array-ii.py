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

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        while i < len(nums) - 2:
            if nums[i] == nums[i + 1] == nums[i + 2]:
                nums[i] = None
            i += 1
        return self.removeElement(nums, None)


def solve(arr):
    print arr
    res = Solution().removeDuplicates(arr)
    print res, arr[:res], arr


solve([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
solve([1, 1, 1, 2])
solve([1, 1, 1])
solve([1, 2, 2, 2])
solve([1])
solve([])
solve([1, 1, 1, 2, 2, 3])
solve([0, 0, 1, 1, 1, 1, 2, 3, 3])
