class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_1 = float('inf')
        num_2 = float('inf')
        for i in nums:
            if i <= num_1:
                num_1 = i
            elif i <= num_2:
                num_2 = i
            else:
                return True
        return False


print Solution().increasingTriplet([1, 2, 3, 4, 5])
print Solution().increasingTriplet([5, 4, 3, 2, 1])
print Solution().increasingTriplet([1, 2])
print Solution().increasingTriplet([2, 1, 5, 0, 3])
print Solution().increasingTriplet([5, 1, 5, 5, 2, 5, 4])
