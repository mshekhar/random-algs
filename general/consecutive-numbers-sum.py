class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """

        res = 1
        for k in xrange(2, int((2 * N) ** 0.5) + 1):
            if (N - (k * (k - 1) / 2)) % k == 0:
                # print k, (N - (k * (k - 1) / 2))
                res += 1
        return res


print Solution().consecutiveNumbersSum(15)
print Solution().consecutiveNumbersSum(5)
print Solution().consecutiveNumbersSum(9)
