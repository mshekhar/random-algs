class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []

        ranges = []
        prev = nums[0]
        start = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != prev + 1:
                if start == prev:
                    ranges.append(str(prev))
                else:
                    ranges.append(str(start) + "->" + str(prev))
                start = nums[i]
            # print nums[i], ranges, start, prev
            prev = nums[i]

        if start == prev:
            ranges.append(str(prev))
        else:
            ranges.append(str(start) + "->" + str(prev))
        return ranges


print Solution().summaryRanges([0, 1, 2, 4, 5, 7])
print Solution().summaryRanges([0, 2, 3, 4, 6, 8, 9])
print Solution().summaryRanges([1])
print Solution().summaryRanges([])
