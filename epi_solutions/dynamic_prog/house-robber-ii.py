class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) < 2:
            return nums[0]
        dp_first_house = [nums[0], max(nums[0], nums[1])]
        dp_not_first_house = [0, nums[1]]

        for i in range(2, len(nums) - 1):
            dp_first_house.append(max(dp_first_house[i - 2] + nums[i], dp_first_house[i - 1]))
        dp_first_house.append(dp_first_house[-1])

        for i in range(2, len(nums)):
            dp_not_first_house.append(max(dp_not_first_house[i - 2] + nums[i], dp_not_first_house[i - 1]))

        return max(dp_first_house[-1], dp_not_first_house[-1])


print Solution().rob([])
