class Solution(object):
    def backtrack(self, nums, res, ele_list, start):
        res.append(ele_list[:])
        i = start
        while i < len(nums):
            ele_list.append(nums[i])
            self.backtrack(nums, res, ele_list, i + 1)
            # print 'popping ele ', ele_list[-1], ele_list
            ele_list.pop()
            # print 'backtrack returned ', i, nums[i], ele_list
            i += 1

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        self.backtrack(nums, res, [], 0)
        return res


print Solution().subsets([1, 2, 3])
