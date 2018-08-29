import math


class Solution(object):
    dp_sum = [0]

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < len(self.dp_sum):
            return self.dp_sum[n]
        # print n, len(self.dp_sum), self.dp_sum
        for i in xrange(len(self.dp_sum), n + 1):
            for j in range(1, int(math.sqrt(i)) + 1):
                # print i, j, i - j * j
                if i == len(self.dp_sum):
                    self.dp_sum.append(self.dp_sum[i - j * j] + 1)
                else:
                    self.dp_sum[i] = min(self.dp_sum[i], self.dp_sum[i - j * j] + 1)
        # print dp_sum
        return self.dp_sum[n]


print Solution().numSquares(13)
print Solution().numSquares(12)
