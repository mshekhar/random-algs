class Solution(object):

    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ele_1 = ele_2 = None
        ele_1_count = ele_2_count = 0
        for n in nums:
            if ele_1 == n:
                ele_1_count += 1
            elif ele_2 == n:
                ele_2_count += 1
            elif ele_1_count == 0:
                ele_1 = n
                ele_1_count = 1
            elif ele_2_count == 0:
                ele_2 = n
                ele_2_count = 1
            else:
                ele_1_count -= 1
                ele_2_count -= 1
            # print ele_1, ele_1_count, ele_2, ele_2_count
        return [n for n in [ele_1, ele_2] if nums.count(n) > len(nums) / 3]


print Solution().majorityElement([1, 1, 1, 2, 3, 4, 5, 6])

# print Solution().majorityElement([1, 1, 1, 3, 3, 2, 2, 2])
# print Solution().majorityElement([3, 2, 3])
