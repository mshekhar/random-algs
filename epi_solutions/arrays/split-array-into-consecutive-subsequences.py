class Solution(object):
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        prev = curr = float('-inf')
        p1 = p2 = p3 = c1 = c2 = c3 = 0
        i = 0
        while i < len(nums):
            num_counter = 0
            curr = nums[i]
            while i < len(nums) and curr == nums[i]:
                num_counter += 1
                i += 1
            if curr != prev + 1:
                if p1 != 0 or p2 != 0:
                    return False
                c1 = num_counter
                c2 = 0
                c3 = 0
            else:
                if num_counter < p1 + p2:
                    return False
                c1 = max(0, num_counter - (p1 + p2 + p3))
                c2 = p1
                c3 = p2 + min(p3, num_counter - (p1 + p2))

            p1 = c1
            p2 = c2
            p3 = c3
            prev = curr
        return p1 == 0 and p2 == 0


print Solution().isPossible([1, 2, 3, 3, 4, 5])
print Solution().isPossible([1, 2, 3, 3, 4, 4, 5, 5])
print Solution().isPossible([1, 2, 3, 4, 4, 5])
