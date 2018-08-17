class Solution(object):
    def is_result_less_than_eq_zero(self, nums):
        for i in nums:
            if i > 0:
                return False

        # import pdb
        # pdb.set_trace()
        negative = True if nums[0] < 0 else False
        for c, i in enumerate(nums):
            if c > 0:
                if i < 0:
                    if negative and True:
                        return False
                    negative = True
                else:
                    negative = False
        return True

    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return nums[0]
        elif self.is_result_less_than_eq_zero(nums):
            print 'result less than'
            return max(nums)
        n = len(nums)
        max_ending_here = 1
        min_ending_here = 1
        max_so_far = 1
        zero_present = False
        for i in range(0, n):
            if nums[i] > 0:
                max_ending_here = max_ending_here * nums[i]
                min_ending_here = min(min_ending_here * nums[i], 1)
            elif nums[i] == 0:
                max_ending_here = 1
                min_ending_here = 1
                zero_present = True
            else:
                temp = max_ending_here
                max_ending_here = max(min_ending_here * nums[i], 1)
                min_ending_here = temp * nums[i]
            if max_so_far < max_ending_here:
                max_so_far = max_ending_here
        return max(max_so_far, 0 if zero_present else float('-inf'))


print Solution().maxProduct([-2, 0, -1])
print Solution().maxProduct([2, 3, -2, 4])
print Solution().maxProduct([-4, -3, -2])
print Solution().maxProduct([2, -5, -2, -4, 3])
print Solution().maxProduct([-4, -3])
