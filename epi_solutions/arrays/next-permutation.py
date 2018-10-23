class Solution(object):
    def reverse_in_place(self, arr, start=0, end=None):
        end = end or len(arr) - 1
        i = start
        j = end
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1

        # print i, nums[i]
        if i - 1 < 0:
            self.reverse_in_place(nums)
            return

        pivot = nums[i - 1]
        j = len(nums) - 1
        while j >= i:
            if nums[j] > pivot:
                break
            j -= 1
        nums[j], nums[i - 1] = nums[i - 1], nums[j]
        # print nums, i, nums[i]
        self.reverse_in_place(nums, start=i)
        # print j, nums[j], pivot
        # print nums

    def runner(self, nums):
        print nums
        self.nextPermutation(nums)
        print nums
        print '\n'


Solution().runner([1, 2, 1, 5, 4, 3, 3, 2, 1])
Solution().runner([5, 4, 3, 3, 2, 1])
Solution().runner([1, 2, 3])
Solution().runner([3, 2, 1])
Solution().runner([1, 1, 5])
