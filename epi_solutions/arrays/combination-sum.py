class Solution(object):
    def backtrack(self, nums, res, ele_list, start, target):
        if target == 0:
            res.append(ele_list[:])
        if target < 0:
            return
        i = start
        while i < len(nums):
            ele_list.append(nums[i])
            self.backtrack(nums, res, ele_list, i, target - nums[i])
            ele_list.pop()
            i += 1

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        res = []
        candidates.sort()
        self.backtrack(candidates, res, [], 0, target)
        return res


print Solution().combinationSum([2, 3, 6, 7], 7)
print Solution().combinationSum([2, 3, 5], 8)
