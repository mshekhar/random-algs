class Solution(object):
    def backtrack(self, nums, res, ele_list, index_ignore_set):
        if len(ele_list) == len(nums):
            res.append(ele_list[:])
        i = 0
        while i < len(nums):
            if i in index_ignore_set:
                i += 1
                continue
            ele_list.append(nums[i])
            index_ignore_set.add(i)
            self.backtrack(nums, res, ele_list, index_ignore_set)
            ele_list.pop()
            index_ignore_set.remove(i)
            i += 1

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        self.backtrack(nums, res, [], set())
        return res


print Solution().permute([1, 2, 3])
