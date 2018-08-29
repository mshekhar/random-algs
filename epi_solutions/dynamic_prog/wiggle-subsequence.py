class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0
        if len(nums) < 2:
            return 1
        last_positive_idx = -1
        last_negative_idx = -1

        wiggle_length = [0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                if last_negative_idx > -1:
                    wiggle_length.append(wiggle_length[last_negative_idx] + 1)
                    last_positive_idx = i
                else:
                    wiggle_length.append(1)
                    last_positive_idx = i
            elif nums[i] < nums[i - 1]:
                if last_positive_idx > -1:
                    wiggle_length.append(wiggle_length[last_positive_idx] + 1)
                    last_negative_idx = i
                else:
                    wiggle_length.append(1)
                    last_negative_idx = i
            else:
                wiggle_length.append(0)
        return max(wiggle_length) + 1


print Solution().wiggleMaxLength([0, 0])
