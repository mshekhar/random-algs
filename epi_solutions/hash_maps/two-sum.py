class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        h = {}
        if len(nums) < 2:
            return []
        for c, n in enumerate(nums):
            if n not in h:
                h[n] = []
            h[n].append(c)

        for c, n in enumerate(nums):
            if target - n in h:
                for ci in h[target - n]:
                    if ci != c:
                        return [c, ci]
        return []


print Solution().twoSum([2, 7, 11, 15], 9)
print Solution().twoSum([3, 5, 2, -4, 8, 11], 7)
print Solution().twoSum([1, 4, 45, 6, 10, 8], 16)
