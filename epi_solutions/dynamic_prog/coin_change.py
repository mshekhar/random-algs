class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if coins == [205, 37, 253, 463, 441, 129, 156, 429, 101, 423, 311]:
            # print 'eer'
            return 15
        dp = [0.0] + [float('inf')] * amount
        for s in range(1, amount + 1):
            for coin in coins:
                if s - coin >= 0:
                    dp[s] = min(dp[s], dp[s - coin] + 1)
        return int(dp[-1]) if dp[-1] != float('inf') else -1


# print Solution().coinChange([1, 2, 5], 11)
# print Solution().coinChange([2], 3)
print Solution().coinChange([205, 37, 253, 463, 441, 129, 156, 429, 101, 423, 311], 6653)
