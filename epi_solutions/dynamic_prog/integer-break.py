class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 1 or n == 2:
            return 1
        if n == 3:
            return 2
        if n == 4:
            return 4

        product = 1
        while n > 4:
            product *= 3
            n -= 3
        return product * n
