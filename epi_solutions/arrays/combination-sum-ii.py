class Solution(object):
    def backtrack(self, nums, res, ele_list, start, target):
        if target == 0:
            res.append(ele_list[:])
        if target < 0:
            return
        i = start
        while i < len(nums):
            if i > start and nums[i] == nums[i - 1]:
                # print 'skipping ', nums[i], i, start, ele_list
                i += 1
                continue
            ele_list.append(nums[i])
            self.backtrack(nums, res, ele_list, i + 1, target - nums[i])
            ele_list.pop()
            i += 1

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        res = []
        candidates.sort()
        self.backtrack(candidates, res, [], 0, target)
        return res


print Solution().combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
print Solution().combinationSum2([2, 5, 2, 1, 2], 5)
print Solution().combinationSum2([2, 3, 6, 7], 7)
print Solution().combinationSum2([2, 3, 5], 8)
