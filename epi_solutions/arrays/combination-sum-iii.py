class Solution(object):
    def backtrack(self, nums, res, ele_list, start, target, set_size):
        if target == 0 and len(ele_list) == set_size:
            res.append(ele_list[:])
        if target < 0:
            return
        i = start
        while i < len(nums):
            ele_list.append(nums[i])
            self.backtrack(nums, res, ele_list, i + 1, target - nums[i], set_size)
            ele_list.pop()
            i += 1

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        self.backtrack(range(1, 10), res, [], 0, n, k)
        return res


print Solution().combinationSum3(3, 7)
print Solution().combinationSum3(3, 9)
