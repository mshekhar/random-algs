class Solution(object):
    def backtrack(self, nums, res, ele_list, start):
        res.append(ele_list[:])
        i = start
        while i < len(nums):
            if i > start and nums[i] == nums[i - 1]:
                # print 'skipping ', nums[i], i, start, ele_list
                i += 1
                continue
            ele_list.append(nums[i])
            self.backtrack(nums, res, ele_list, i + 1)
            ele_list.pop()
            i += 1

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        self.backtrack(nums, res, [], 0)
        return res


print Solution().subsetsWithDup([1, 2, 2, 3])
