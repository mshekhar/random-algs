class Solution(object):
    def knightDialer(self, N):
        """
        :type N: int
        :rtype: int
        """

        dp = [1] * 10
        reachable_nums = {
            0: (4, 6),
            1: (6, 8),
            2: (7, 9),
            3: (4, 8),
            4: (3, 9, 0),
            5: (),
            6: (0, 1, 7),
            7: (2, 6),
            8: (1, 3),
            9: (2, 4)
        }
        nums = range(10)
        for _ in xrange(N - 1):
            tmp_dp = [0] * 10
            for i in nums:
                tmp_dp[i] = sum([dp[x] % (10 ** 9 + 7) for x in reachable_nums[i]])
            dp = tmp_dp
        return sum(dp) % (10 ** 9 + 7)


# print Solution().knightDialer(3)
# print Solution().knightDialer(1)
# print Solution().knightDialer(2)
print Solution().knightDialer(4980)
