class Solution(object):
    def get_total(self, N, K, W):
        i = K - W
        point_max = W
        total = 0
        while i < K:
            if i >= 0:
                total += W - point_max + 1
                # print 'total ', i, point_max, total
            i += 1
            point_max -= 1
        return total

    def get_less_than_n(self, N, K, W):
        i = N + 1 - W
        point_max = W
        less_than_n = 0
        while i < K:
            if i >= 0:
                less_than_n += W - point_max + 1
                # print 'less than n ', i, point_max, less_than_n
            i += 1
            point_max -= 1
        return less_than_n

    def new21Game(self, N, K, W):
        """
        :type N: int
        :type K: int
        :type W: int
        :rtype: float
        """
        less_than_n = self.get_less_than_n(N, K, W)
        total = self.get_total(N, K, W)

        # print less_than_n, total, 1 - (less_than_n * 1.0 / total)
        try:
            return 1 - (less_than_n * 1.0 / total)
        except ZeroDivisionError:
            return 0


print Solution().new21Game(21, 17, 10)
print Solution().new21Game(0, 0, 1)
# Solution().new21Game(6, 1, 10)
# Solution().new21Game(10, 1, 10)
