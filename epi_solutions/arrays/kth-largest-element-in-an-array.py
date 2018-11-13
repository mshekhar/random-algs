import random


class Solution(object):
    def quick_select_kth_largest(self, nums, k, start, end):
        pivot_ele = nums[end]
        n = (end - start) + 1
        i = j = start
        while j < end:
            if nums[j] <= pivot_ele:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
            j += 1
        nums[i], nums[end] = nums[end], nums[i]
        m = (i - start) + 1
        if m == n - k + 1:
            return nums[i]
        elif m < n - k + 1:
            return self.quick_select_kth_largest(nums, k, i + 1, end)
        return self.quick_select_kth_largest(nums, k - (n - m + 1), start, i - 1)

    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        random.shuffle(nums)
        return self.quick_select_kth_largest(nums, k, 0, len(nums) - 1)

    @classmethod
    def runner(cls):
        arrs = [
            [3, 2, 1, 5, 6, 4],
            [3, 2, 3, 1, 2, 4, 5, 5, 6],
            [7, 10, 4, 3, 20, 15],
            [10, 4, 5, 8, 6, 11, 26]
        ]
        for arr in arrs:
            sorted_arr = sorted(arr, reverse=True)
            for i in xrange(1, len(arr) + 1):
                for j in xrange(100):
                    res = Solution().findKthLargest(arr, i)
                    assert res == sorted_arr[i - 1]


Solution.runner()

print Solution().findKthLargest([1], 1)
print Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2)
print Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
print Solution().findKthLargest([7, 10, 4, 3, 20, 15], 3)
print Solution().findKthLargest([7, 10, 4, 3, 20, 15], 4)
print Solution().findKthLargest([10, 4, 5, 8, 6, 11, 26], 3)
