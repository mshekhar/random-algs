class Solution(object):
    def __init__(self):
        self.dp = {0: 0, 1: 1, 2: 1}
        self.pow_2_counter = 1
        {2: 1, 3: 2, 4: 1, 5: 2, 6: 2, 7: 3, 8: 1,
         9: 2, 10: 2, 11: 3, 12: 2, 13: 3, 14: 3, 15: 4, 16: 1}

    def helper(self, n):
        if n in self.dp:
            return self.dp[n]
        closest_2_pow = 2 ** self.pow_2_counter
        rem = n - closest_2_pow
        # print 'calling helper', n, rem
        if rem == 0 or closest_2_pow == rem:
            self.pow_2_counter += 1
            self.dp[n] = 1
        else:
            self.dp[n] = 1 + self.helper(rem)
        return self.dp[n]

    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        if num < 0:
            return []
        sol = []
        for i in range(num + 1):
            sol.append(self.helper(i))
        return sol


s = Solution()
print s.countBits(5)
# print s.dp, s.pow_2_counter
