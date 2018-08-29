class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 0
        for i in range(2, n):
            if not n % i:
                return i + self.minSteps(n / i)
        return n


print Solution().minSteps(3)
