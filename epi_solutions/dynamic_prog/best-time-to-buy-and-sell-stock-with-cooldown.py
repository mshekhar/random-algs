class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) < 2:
            return 0
        buy = [None] * len(prices)
        sell = [None] * len(prices)

        buy[0] = -prices[0]
        sell[0] = 0
        buy[1] = max(buy[0], - prices[1])
        sell[1] = max(sell[0], buy[0] + prices[1])

        for i in range(2, len(prices)):
            # print i, buy, sell
            buy[i] = max(buy[i - 1], sell[i - 2] - prices[i])
            sell[i] = max(sell[i - 1], buy[i - 1] + prices[i])

        return sell[-1]


print Solution().maxProfit([1, 2, 3, 0, 2])
