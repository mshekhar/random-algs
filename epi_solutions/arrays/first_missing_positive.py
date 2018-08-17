class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr = 0
        while curr < len(nums):
            if nums[curr] > 0 and not nums[curr] - 1 == curr:
                idx = nums[curr] - 1
                if idx <= len(nums) - 1 and nums[idx] != nums[curr]:
                    tmp = nums[idx]
                    nums[idx] = nums[curr]
                    nums[curr] = tmp
                    if nums[curr] - 1 == curr:
                        curr += 1
                else:
                    nums[curr] = -1
            else:
                curr += 1
        print nums
        for c, i in enumerate(nums):
            if i != c + 1:
                return c + 1
        return len(nums) + 1


print Solution().firstMissingPositive([1, 2, 0]), 3
print Solution().firstMissingPositive([3, 4, -1, 1]), 2
print Solution().firstMissingPositive([7, 8, 9, 11, 12]), 1
print Solution().firstMissingPositive([1, 2, 3]), 4
print Solution().firstMissingPositive([1, 1]), 2
