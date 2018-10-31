class Solution(object):
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """

        for c, i in enumerate(A):
            if abs(i - c) > 1:
                return False
        return True


print Solution().isIdealPermutation([1, 2, 0])
