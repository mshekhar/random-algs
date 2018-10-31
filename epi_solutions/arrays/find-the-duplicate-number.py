class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        lo = 0
        hi = len(nums) - 1

        while lo < hi:
            mid = (hi + lo) / 2
            count = 0
            for i in nums:
                if i <= mid:
                    count += 1
            if count <= mid:
                lo = mid + 1
            else:
                hi = mid
        return lo


print Solution().findDuplicate([1, 3, 4, 2, 2])
print Solution().findDuplicate([3, 1, 3, 4, 2])
