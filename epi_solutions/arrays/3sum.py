class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if len(nums) < 3:
            return []
        all_zeros = True
        for i in nums:
            all_zeros = all_zeros and not i
        if all_zeros:
            return [[0, 0, 0]]
        h = {}
        sol_h = set()
        for i in nums:
            if i not in h:
                h[i] = 0
            h[i] += 1
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                s = nums[i] + nums[j]
                if -s in h:
                    if (nums[i] == -s and nums[j] == -s) and h[-s] < 3:
                        continue
                    if (nums[i] == -s or nums[j] == -s) and h[-s] < 2:
                        continue
                    sol_h.add(tuple(sorted([nums[i], nums[j], -s])))
        return list(sol_h)


# print Solution().threeSum([-1, 0, 1, 2, -1, -4]), [[-1, 0, 1], [-1, -1, 2]]
# print Solution().threeSum([0, -1, 2, -3, 1]), [[0, -1, 1], [2, -3, 1]]
# print Solution().threeSum([1, -2, 1, 0, 5]), [1, -2, 1]
# print Solution().threeSum([0, 0, 0]), [[0, 0, 0]]
print Solution().threeSum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]]
print Solution().threeSum([-1, 0, 1, 0]), [[-1, 0, 1]]
